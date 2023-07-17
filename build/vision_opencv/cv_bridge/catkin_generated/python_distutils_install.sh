#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/lzc/lzc-code/src/vision_opencv/cv_bridge"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/lzc/lzc-code/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/lzc/lzc-code/install/lib/python3/dist-packages:/home/lzc/lzc-code/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/lzc/lzc-code/build" \
    "/usr/bin/python3" \
    "/home/lzc/lzc-code/src/vision_opencv/cv_bridge/setup.py" \
    egg_info --egg-base /home/lzc/lzc-code/build/vision_opencv/cv_bridge \
    build --build-base "/home/lzc/lzc-code/build/vision_opencv/cv_bridge" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/lzc/lzc-code/install" --install-scripts="/home/lzc/lzc-code/install/bin"
