# -*- coding: utf-8 -*-

name = "appleseed.maya"

version = "1.0.1"

description = "appleseed-maya"

requires = [
    "appleseed"
]

def commands():
    env.MAYA_PLUG_IN_PATH.append("{root}/plug-ins/" + str(resolve.maya.version))
    env.MAYA_SCRIPT_PATH.append("{root}/scripts")
    env.PYTHONPATH.append("{root}/scripts")
    env.XBMLANGPATH.append("{root}/icons/%B")
    env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/maya")
    env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/appleseed")
    env.APPLESEED_SEARCHPATH.append("{root}/procedurals")
    env.MAYA_RENDER_DESC_PATH.append("{root}/renderDesc")
    env.MAYA_PRESET_PATH.append("{root}/presets")
    env.MAYA_CUSTOM_TEMPLATE_PATH.append("{root}/scripts/appleseedMaya/AETemplates")
    env.MAYA_SHELF_PATH.append("{root}/prefs/shelves")

    # Disable signal handlers while developing.
    env.MAYA_DEBUG_NO_SIGNAL_HANDLERS.set("1")

    # Enable debugging while developing.
    env.APPLESEED_MAYA_LOG_LEVEL.set("debug")
