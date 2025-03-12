# grub2-mkconfig命令

```sh
grub2-mkconfig -o /boot/grub2/grub.cfg   # BIOS（leagcy）引导
grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg   # UEFI引导
```