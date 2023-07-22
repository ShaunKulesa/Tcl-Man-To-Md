# NAME

Tk_GetVRootGeometry - Get location and size of virtual root for window

# SYNOPSIS

**#include \<tk.h\>**

**Tk_GetVRootGeometry(***tkwin, xPtr, yPtr, widthPtr, heightPtr***)**

# ARGUMENTS

Token for window whose virtual root is to be queried.

Points to word in which to store x-offset of virtual root.

Points to word in which to store y-offset of virtual root.

Points to word in which to store width of virtual root.

Points to word in which to store height of virtual root.

# DESCRIPTION

**Tk_GetVRootGeometry** returns geometry information about the virtual
root window associated with *tkwin*. The virtual root is the one in
which *tkwin*\'s nearest top-level ancestor (or *tkwin* itself if it is
a top-level window) has been reparented by the window manager. This
window is identified by a **\_\_SWM_ROOT** or **\_\_WM_ROOT** property
placed on the top-level window by the window manager. If *tkwin* is not
associated with a virtual root (e.g. because the window manager does not
use virtual roots) then \**xPtr* and \**yPtr* will be set to 0 and
\**widthPtr* and \**heightPtr* will be set to the dimensions of the
screen containing *tkwin*.

# KEYWORDS

geometry, height, location, virtual root, width, window manager
