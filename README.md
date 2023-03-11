# Dotfile & Configs


## Arch installation

Set your hostname in /etc/hostname.
Example:

```bash
fernando-arch
```

Set your localhost in /etc/hosts:

```bash
127.0.0.1        localhost
::1              localhost
127.0.1.1        myhostname
```

Network manager

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Grub Intall/Config:

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Create your user:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,optical,storage username
```

To have root privileges we need sudo:

```bash
sudo pacman -S sudo
```

Now you can reboot:

```bash
exit
umount -R /mnt
reboot
```

After logging in, your internet should be working just fine, but if your computer not have port Ethernet, it will be necessary to connect to the internet via terminal with NetworkManager.

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

environments is installing Xorg:

```bash
sudo pacman -S xorg
```


## Login and window manager

```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile picom alacritty chromium
```


After enabling lightdm we can restart the computer.

```bash
systemctl enable lightdm
reboot
```


## Apps

| Software     | Utility                 |
|--------------|-------------------------|
| **neovim**   | Terminal based editor   |
| **thunar**   | Graphical file explorer |
| **ranger**   | Terminal based explorer |
| **rofi**     | Menu and widow switcher |
| **scrot**    | Screenshot              |
| **redshift** | Take care of your eyes  |


### Audio

```bash
sudo pacman -S pulseaudio pavucontrol pamixer
```


### Bright manager

```bash
sudo pacman -S brightnessctl
```


### Fonts

```bash
yay -S ttf-scientifica ttf-firacode-nerd ttf-mononoki-nerd
```


## Xprofile

```bash
sudo pacman -S xorg-xinit
```

Append this in ~/.xprofile:

```bash
setxkbmap br &
picom &
```


## Theme

```bash
yay -S nordic-theme
```

GUI for changing

```bash
sudo pacman -S lxappearance
```
