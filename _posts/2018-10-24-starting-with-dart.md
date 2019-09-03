---
layout: post
title:  "Starting with DART (Dynamic Animation and Robotics Toolkit)"
tags: ["dart", "simulation", "how to"]
author: "Anthony J. Clark"
---

In this post, I will be showing how to simulating a falling sphere using [DART](https://dartsim.github.io/). For this simple example, I will not be worrying about any form of visualization. This post is mostly intended to help me document and remember how to setup a simple simulation.

I have used a variety of different simulation packages for my research, and I've never been overly satisfied with the two that I have used most often: [Open Dynamics Engine (ODE)](https://www.ode-wiki.org/wiki/) and [MATLAB/Simulink](https://www.mathworks.com/). ODE is open source and it works well, but it is a game engine with an emphasis on speed and not necessarily on accuracy. Simulink, on the other hand, requires you to pay for both it and MATLAB, and it focuses on numerical simulation (not physical simulation). I'll likely still use the tools going forward, however [Jean-Baptiste Mouret's](https://members.loria.fr/JBMouret/) talk at [SimER](http://cis.gvsu.edu/~moorejar/SimER/) this past July convinced me to give DART a try.

# Installing DART

On a mac, installing should be as simple as:

```bash
brew install dartsim6
```

However, I generally prefer to only install optional dependencies that I know I'll use. So, I first tried to install like so:

```bash
brew install dartsim6 --without-gui \
                      --without-gui-osg \
                      --without-optimizer-ipopt \
                      --without-optimizer-nlopt \
                      --without-planning \
                      --without-utils \
                      --without-utils-urdf
```

You can see all of the options with:

```bash
brew info dartsim6
```

I consider installing with [brew](https://brew.sh/) the ideal scenario for my platform. However, on my system [I ran into a strange issue](https://github.com/dartsim/dart/issues/946). So, I ended up installing like so:

```bash
hub clone dartsim/dart
cd dart/
git checkout tags/v6.3.0
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/path/to/local/installation ..
make install
```

I installed DART into a non-standard local location so that I could easily delete it once I eventually get it installed using brew (once the issue has been fixed). Installing to a non-standard location does require a bit of extra working during compiling. Specifically, I had to add the lib folder to `DYLD_LIBRARY_PATH`.


# DART In C++

In case you want to follow along as I step through building the sphere simulation, I will start by providing the includes, main function, and show how to compile.

This is pretty standard stuff, we will only be using `dart` and printing to `STDOUT`.

```cpp
#include <dart/dart.hpp>
#include <iostream>

int main()
{
    constexpr double density = 1.0;
    constexpr double radius = 0.3;
    constexpr double restitution = 0.9;
    constexpr double damping = 0.1;
    constexpr double starting_height = 10.0;
    const std::string name{"sphere1"};

    // Rest of code...
}
```

I created a [simple build script](https://github.com/anthonyjclark/DART-examples/blob/master/build.sh) for compiling the project. You could also go with a plain makefile or CMake, but for small projects I prefer to write a simple script. The compile command ends up looking something like this:

```bash
clang++ -std=c++14 -Wall -Wextra -Wl,-search_paths_first -Wl,-headerpad_max_install_names -Wl,-rpath,/Users/ajc/.local/lib -isystem/usr/local/include/eigen3 -isystem/Users/ajc/.local/include -isystem/usr/local/include/bullet -L/Users/ajc/.local/lib -ldart -lassimp -lBulletCollision -lLinearMath -ldart-collision-bullet sphere/sphere.cpp -o bin/sphere
```


# A Falling Sphere

For this simple example, I am just going to have a sphere fall and then bounce on a static ground plane. The [source can be found in this repository](https://github.com/anthonyjclark/DART-examples), but I will be stepping through each part of the simple example here.

To create a sphere, we need to start with a `Skeleton`.

```cpp
dart::dynamics::SkeletonPtr sphere = dart::dynamics::Skeleton::create(name);
```

A `Skeleton` acts as a container for several objects. Any shapes that you want to be grouped together (for example, the chassis and wheels of a vehicle) can be added to a single skeleton.

Next, we need to create a `SphereShape`:

```cpp
dart::dynamics::ShapePtr sphere_shape(new dart::dynamics::SphereShape(radius));
```

This object represents a geometry that can be used to calculate sphere properties (volume, inertia tensor, etc.) and will eventually be used to create a `BodyNode` with dynamic and collisions aspects.

To create the sphere, we need to define both a `Joint` and a `Body`. The `Joint` attaches the sphere to another `Body`, or to a `World` when the body doesn't need to connect to another dynamic or static object; one `Joint` is required for every `Body`. In this case, we want the sphere to free fall, so we attach it to the `World` using a `FreeJoint`.

To help initialize these entities, we can use a `FreeJoint::Properties` object:

```cpp
dart::dynamics::FreeJoint::Properties sphere_joint_prop;
sphere_joint_prop.mDampingCoefficients = Eigen::Vector6d::Constant(damping);

dart::dynamics::BodyNode::Properties sphere_body_prop;
sphere_body_prop.mInertia.setMass(sphere_mass);
sphere_body_prop.mInertia.setMoment(sphere_shape->computeInertia(sphere_mass));
sphere_body_prop.mRestitutionCoeff = restitution;
```

In the snippet above I set a few properties for our `Joint` and `Body`. Regarding the sphere's `FreeJoint`, you can think of damping as adding wind resistance. In this case I have added damping to all 6 degrees-of-freedom (rotation and translation), which doesn't necessarily make physical sense, but it serves as a good example. Likewise, for the `Body` I have added inertial properties and a [coefficient of restitution](https://en.wikipedia.org/wiki/Coefficient_of_restitution).

Next, we create the `Joint` and `Body`:

```cpp
dart::dynamics::FreeJoint* sphere_joint;
dart::dynamics::BodyNode* sphere_body;

std::tie(sphere_joint, sphere_body) =
    sphere->createJointAndBodyNodePair<dart::dynamics::FreeJoint>(
        nullptr, sphere_joint_prop, sphere_body_prop);
```

The `createJointAndBodyNodePair` method adds a `Body` and `Joint` to a `Skeleton`. I am using [`std::tie`](https://en.cppreference.com/w/cpp/utility/tuple/tie) since the method returns a [`std::pair`](https://en.cppreference.com/w/cpp/utility/pair) and I don't like accessing members through `first` and `second`.

Now that we have a `Body` and a `Joint` we can set the sphere's initial values.

```cpp
sphere_body->createShapeNodeWith<
    dart::dynamics::CollisionAspect,
    dart::dynamics::DynamicsAspect>(
        sphere_shape);

Eigen::Vector6d positions(Eigen::Vector6d::Zero());
positions[5] = starting_height;
sphere_joint->setPositions(positions);
```

The first method call sets the `Shape` of the sphere to the shape that we created above. The second method call sets the starting position of the sphere to a distance that is `starting_height` above the origin.

Finally, we need to create a world and add the sphere to it:

```cpp
dart::simulation::WorldPtr world(new dart::simulation::World);
world->addSkeleton(sphere);
```

At this point, we could add a few calls to `world->step()` and everything should work as expected (the sphere would fall). However, since the sphere falling straight down for eternity (or for however many time steps you set) is not very interesting we are going to add a ground plane.

# A Ground Plane

Since most of this code is repetitive, I am not going to go through this step-by-step:

```cpp
auto ground = dart::dynamics::Skeleton::create("ground");

auto ground_body = ground->createJointAndBodyNodePair<
    dart::dynamics::WeldJoint>(
        nullptr).second;

ground_body->setRestitutionCoeff(restitution);

dart::dynamics::ShapePtr ground_box(new dart::dynamics::BoxShape(
    Eigen::Vector3d(100, 100, 1)));

ground_body->createShapeNodeWith<
    dart::dynamics::CollisionAspect,
    dart::dynamics::DynamicsAspect>(
        ground_box);

world->addSkeleton(ground);
```

The main differences between the sphere and this ground plane is that the ground plane uses a `WeldJoint` to attach it to the world (since it does not move), and it uses a `BoxShape` instead of a `SphereShape`. *Note: DART does have a `PlaneShape`, but it is not supported by the default collision engine ([FCL](https://github.com/flexible-collision-library/fcl))--or at least DART doesn't support FCL's plane type yet.*

# Simulating the Sphere

Now that we have a sphere and a ground plane, all that is left is to run the simulation:

```cpp
constexpr double TIME_STOP = 10;
constexpr double TIME_STEP = 0.001;
world->setTimeStep(TIME_STEP);

while (world->getTime() < TIME_STOP) {
    world->step();
}
```

I removed the print statements from the previous snippet. To see code for getting and printing the position of the sphere [see the source code found here](https://github.com/anthonyjclark/DART-examples/blob/4c3c1c82bde7a2fa49cde16558d5f5a17998e207/sphere/sphere.cpp#L133-L143).

The figure below shows results from this simulation with different values for the coefficient of restitution and wind drag (i.e., damping on the `FreeJoint`).

![Falling Sphere, Position vs. Time](/assets/2018-10-24-starting-with-dart/sphere_chart.png)

A few things to note in the above figure:

- With a restitution value of 1.0, the sphere bounces exactly up to its original height.
- With a restitution value above 1.0, the sphere will continue bouncing higher and higher.
- With a restitution value below 1.0, the sphere will start to bounce lower and lower.
- With added drag, the sphere falls more slowly and bounces less high.

# Notes

DART is still under active development and I wouldn't quite consider it completely mature (the API is still subject to rapid changes). Even in this short example I found a few oddities. First, DART has a default constructor for `BodyNode` properties (that can be passed to `createJointAndBodyNodePair`) called `BodyNode::AspectProperties()`, but the corresponding `FreeJoint::AspectProperties()` cannot be passed to the same function. I'm sure this is my user error, but the naming convention leaves something to be desired.

I am also not a fan of how freely they mix raw pointers and smart pointers. `createJointAndBodyNodePair` returns raw pointers while most other methods in this example return `std::shared_ptr`. This may have something to due with performance, but I did not find an explanation in the DART documentation.
