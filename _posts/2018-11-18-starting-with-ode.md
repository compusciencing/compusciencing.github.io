---
layout: post
title:  "Starting with ODE (Open Dynamics Engine)"
tags: ["ode", "simulation", "how to"]
author: "Anthony J. Clark"
---

In this post I will be giving a minimal example of using [ODE (the Open Dynamics Engine)](https://www.ode-wiki.org/wiki/index.php?title=Main_Page). This is similar to [my last post about DART]({{ site.baseurl }}{% post_url 2018-10-24-starting-with-dart %}). The main purpose is to serve as a quick reference for setting up a simulation in ODE without all of the extra stuff included in the ODE examples (like the Drawstuff library).


# Installing ODE

You can download the ODE source code from [odedevs](https://bitbucket.org/odedevs/ode/downloads/). For this post I am using version `0.15.2`.

`INSTALL.txt` includes instructions on how to build and install the library, and below I show how I installed ODE to a local directory on my Unix machine. I prefer to play around with a new piece of software (or new version of software) in a local directory instead of installing in a system location:

```bash
./configure --prefix=/Users/ajc/Documents/projects/simulators/local/ --enable-double-precision

make
make install
```

ODE has quite a few options, and you can see above that I enable double-precision floating point numbers with `--enable-double-precision`. To see a list of all options you would type: `./configure --help`.

Unless you decided to build ODE without demos (`--disable-demos`), you should now be able to play around with all of the demos that come with ODE.

```bash
cd into/the/ode/directory
cd ode/demo/
./demo_hinge
```

# ODE In C++

In case you want to follow along as I step through building the sphere simulation, I will start by providing the includes, main function, and show how to compile.

This is pretty standard stuff, we will only be using `ode` and printing to `STDOUT`.

```cpp
#include <ode/ode.h>
#include <iostream>

int main()
{
  constexpr dReal density = 1.0;
  constexpr dReal radius = 0.3;
  constexpr dReal starting_height = 10.0;
  constexpr dReal gravity_y = -9.81;

  // Code for simulating sphere
}
```

ODE offers a pretty simple C-style API. Though you can find object-oriented wrappers (and Python bindings).

Unlike the DART example, for ODE I am using CMake to build my projects (actually, I am using CLion, which in turn uses CMake). Here is my `CMakeLists.txt` file:

```cmake
cmake_minimum_required(VERSION 3.12)
project(sphere)

set(CMAKE_CXX_STANDARD 17)

add_executable(sphere main.cpp)

# Add ODE library
include_directories("/Users/ajc/Documents/projects/simulators/local/lib/")
target_link_libraries(sphere -lode)
```

ODE is a fairly old-school C++ library that does not require all of the [extra steps required to build a project like DART]({{ site.baseurl }}{% post_url 2018-10-24-starting-with-dart %}#dart-in-c), but it also doesn't provide as many features (e.g., a plug-in interface for using different collision detection libraries).

# A Falling Sphere

For this simple example, I am just going to have a sphere fall and then bounce on a static ground plane. The [source code can be found in this repository](https://github.com/anthonyjclark/ODE-examples), but I will be stepping through each part of the simple example here.

We need to start by initializing ODE and creating a world.

```c++
dInitODE2(0);

dWorldID world = dWorldCreate();
dWorldSetGravity(world, 0.0, gravity_y, 0.0);
```

A `world` in ODE is used to simulate rigid body dynamics--the world is not at all concerned with collisions (except that they add constraints to the simulated dynamics). To allow for collisions between objects we next need to create a collision space.

```c++
dSpaceID space = dSimpleSpaceCreate(0);
dJointGroupID collision_contact_group = dJointGroupCreate(0);
CollisionData collision_data {world, collision_contact_group};
```

A `space` is analogous to the `world` above. It *handles* collisions between objects. Unlike most other physics libraries though, ODE requires you to write a callback function for handling collisions manually. 

The callback function takes an optional pointer to user defined data. For this example, I've used the data pointer to pass in what would otherwise need to be global data. Specifically, the `collision_data` object above is used to package up the `world` and `collision_contact_group` so that they can be passed to the collision handling callback. Here is the definition for the struct and callback:

```c++
struct CollisionData {
  dWorldID world;
  dJointGroupID contact_group;
};

void handle_collisions(void *data, dGeomID geom1, dGeomID geom2)
{
  auto collision_data = static_cast<CollisionData*>(data);

  // Get the rigid bodies associated with the geometries
  dBodyID body1 = dGeomGetBody(geom1);
  dBodyID body2 = dGeomGetBody(geom2);

  // Maximum number of contacts to create between bodies (see ODE documentation)
  const int MAX_NUM_CONTACTS = 8;
  dContact contacts[MAX_NUM_CONTACTS];

  // Add collision joints
  int numc = dCollide(geom1, geom2, MAX_NUM_CONTACTS, &contacts[0].geom, sizeof(dContact));

  for (int i = 0; i < numc; ++i) {

    contacts[i].surface.mode = dContactSoftERP | dContactSoftCFM | dContactApprox1 |
        dContactSlip1 | dContactSlip2;

    contacts[i].surface.mu = 50.0;
    contacts[i].surface.soft_erp = 0.96;
    contacts[i].surface.soft_cfm = 2.00;

    // struct dSurfaceParameters {
    //      int mode;
    //      dReal mu;
    //      dReal mu2;
    //      dReal rho;
    //      dReal rho2;
    //      dReal rhoN;
    //      dReal bounce;
    //      dReal bounce_vel;
    //      dReal soft_erp;
    //      dReal soft_cfm;
    //      dReal motion1, motion2, motionN;
    //      dReal slip1, slip2;
    // };

    dJointID contact = dJointCreateContact(collision_data->world,
        collision_data->contact_group, &contacts[i]);

    dJointAttach(contact, body1, body2);
  }
}
```

Writing your own collision handler has definite benefits (you get a better understanding of collisions and you are forced to come up with your own sensible collision properties) and drawbacks (you don't get to rely on the library to define sensible defaults).

The collision handler is passed in all pairwise rigid bodies and they can each be handled separately. For example, you can attach user data to each collision geometry (described later) defining its physical properties. For this project, I assume that every collision is the same.

Collisions are handled by creating temporary contact joints between bodies. These joints constrain the motion of bodies with respect to one another.

Next up we create the sphere's rigid body.

```c++
dBodyID sphere = dBodyCreate(world);
dBodySetPosition(sphere, 0.0, starting_height, 0.0);

dMass sphere_mass;
dMassSetSphere(&sphere_mass, density, radius);
dBodySetMass(sphere, &sphere_mass);
```

Here you can see why we need to start by defining the `world`. We create a new rigid body and set its inertial properties with `dBodySetMass`.

At this point we could jump to simulating the world, but the sphere wouldn't collide with anything; instead it would just fall forever. So, let's attach a collision object to the rigid body.

```c++
dGeomID sphere_geom = dCreateSphere(space, radius);
dGeomSetBody(sphere_geom, sphere);
```

And now add a ground plane to the same collision space.

```c++
dGeomID ground_geom = dCreatePlane(space, 0, 1, 0, 0);
```

The call to [`dCreatePlane`](https://www.ode-wiki.org/wiki/index.php?title=Manual:_All#Plane_Class) with the given arguments will create an x-z plane with a y value of zero.

# Simulating the Sphere

Now all that is left is to step through time.

```c++
constexpr dReal TIME_STOP = 10;
constexpr dReal TIME_STEP = 0.001;
constexpr dReal OUTPUT_STEP = 0.05;

dReal next_output_time = OUTPUT_STEP;
for (dReal time = 0.0; time < TIME_STOP + TIME_STEP/2.0; time += TIME_STEP) {
  dSpaceCollide(space, &collision_data, &handle_collisions);
  dWorldStep(world, static_cast<dReal>(TIME_STEP));
  dJointGroupEmpty(collision_contact_group);
}
```

At each time step we need to handle collisions (attach collision contact joints), step the dynamic world, and then empty out all contact joints.

The plot below shows the vertical position of the sphere through time.

![Falling Sphere, Position vs. Time](/assets/2018-11-18-starting-with-ode/sphere_chart_ode.png)


# Cleanup

Since ODE offers the C-API, it does require manual cleanup of all created objects. At minimum you should cleanup the following.

```c++
dSpaceDestroy(space);
dWorldDestroy(world);
dCloseODE();
```

