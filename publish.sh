#!/bin/sh

VERSION="0.7.0"

echo "Publishing version $VERSION"

package() {
    python setup.py bdist_wheel
}

upload() {
    twine upload dist/"cxc_toolkit-$VERSION-py3-none-any.whl"
}

package
upload
