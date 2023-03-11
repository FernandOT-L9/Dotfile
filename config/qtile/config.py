from libqtile import bar, layout, widget
from libqtile.config import (
Click,
Drag,
Group,
Key,
Match, 
Screen)
from libqtile.lazy import lazy
from libqtile import qtile


mod = "mod4"

terminal     = 'alacritty'
file_manager = 'thunar'
browser      = 'chromium'


keys = [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Change window sizes (MonadTall)
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Toggle between different layouts as defined below
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    Key([mod], "q", lazy.window.kill()),
    
    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    
    # Window States
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle window between minimum and maximum sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
   
    Key([mod], "h", lazy.window.toggle_minimize(), desc="Toggle minimization on focused window"),
    Key([mod, "shift"], "h", lazy.group.unminimize_all(), desc="Unminimize all windows on current group"),

    # Floating controls
    Key(
        [mod], "bracketleft",
        lazy.group.prev_window(),
        lazy.window.bring_to_front(),
        desc="Cycle previous floating window",
    ),
    Key(
        [mod],
        "bracketright",
        lazy.group.next_window(),
        lazy.window.bring_to_front(),
        desc="Cycle next floating windows",
    ),

    # ------------ App Configs -----------
    
    # Menu
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "space", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn(browser)),

    # File Explorer
    Key([mod], "e", lazy.spawn(file_manager)),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),
    
    # Calculator
    Key(["mod1"], "Return", lazy.spawn("io.elementary.calculator")),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 5000")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pamixer --increase 1 --set-limit 100"
    )),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pamixer --decrease 1 --set-limit 100"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Play / Pause
    Key(
        [mod],
        "XF86AudioMute",
        lazy.spawn("playerctl play-pause")
    ),

    # Play last Audio
    Key(
        [mod],
        "XF86AudioLowerVolume",
        lazy.spawn("playerctl previous")
    ),

    # Play Next Audio
    Key(
        [mod],
        "XF86AudioRaiseVolume",
        lazy.spawn("playerctl next")
    ),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +1%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1%-")),
]

colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]

layout_theme = {
    "border_focus":colors[10],
    "border_normal":colors[0],
    "border_width":3,
    "border_on_single":True,
}

layouts = [
    layout.Bsp(**layout_theme),
    layout.Max(**layout_theme),
]

groups = [
    Group(name="1"),
    Group(name="2"),
    Group(name="3"),
    Group(name="4"),
    Group(name="5"),
] 

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

widget_defaults = dict(
    background='#282A36',
    foreground=colors[7],
    font="scientifica",
    fontsize=25,
)
extension_defaults = widget_defaults.copy()


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


screens = [
    Screen(
        wallpaper="~/Pictures/nasa.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='text',
                    active=colors[1],
                    inactive=colors[10],
                    this_current_screen_border=colors[7],
                    spacing=25,
                    margin_x=20,
                ),
                widget.Spacer(),
                widget.Clock(
                    format='%d/%m %H:%M',
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=23,
                    padding=12,
                ),
                widget.Sep(
                    linewidth=25,
                    foreground='#282A36',
                ),
                widget.PulseVolume(
                    fmt='MUTE  {}',
                    limit_max_volume=True,
                    mouse_callbacks={"Button3": open_pavu},
                ),
                widget.Battery(
                    format='BAT  {percent:2.0%}',
                    padding=30,
                ),
            ],
            40, # Width Bar
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod],"Button1", lazy.window.set_position_floating(), start=lazy.window.get_position(),),
    Drag([mod],"Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod],"Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False

floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pomotroid"),
        Match(wm_class="cmatrixterm"),
        Match(title="Farge"),
        Match(wm_class="thunar"),
        Match(wm_class="feh"),
        Match(wm_class="eog"),
        Match(wm_class="io.elementary.calculator"),
        Match(wm_class="blueberry.py"),
    ],
)

auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#        margin=[3, 0, 0, 0],
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
