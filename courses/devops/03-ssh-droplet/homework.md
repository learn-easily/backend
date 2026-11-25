# სერვერის დაცვა

lms-server — დაცულია და მზადაა შემდეგი ლექციისთვის

## მოთხოვნები

- `apt upgrade` · `00-hardening.conf`: root და პაროლი აკრძალულია → `restart ssh` (ჯერ Termius-ის ახალ tab-ში შეამოწმეთ!)
- `ufw`: მხოლოდ `OpenSSH` → `enable`
- swap 2 GB (`/etc/fstab`-ითაც) · WSL-ში `~/.ssh/config` → `ssh lms`

## ✓ მზადაა, როცა

`sshd -T` — `no`/`no`, `ufw status` — active, `free -h` — Swap 2.0Gi, `ssh lms` შედის

## ⭐ ბონუსი

- `sudo journalctl -u ssh --since "1 hour ago" | grep -i invalid` — ნახეთ, რამდენმა ბოტმა სცადა შესვლა ამ ერთ საათში

## ამოხსნა

```console Termius · lms-server !
$ sudo nano /etc/ssh/sshd_config.d/00-hardening.conf
PermitRootLogin no
PasswordAuthentication no

$ sudo sshd -t                     # ცარიელი პასუხი = OK
$ sudo systemctl restart ssh

$ sudo ufw allow OpenSSH
$ sudo ufw enable
$ sudo ufw status
Status: active
OpenSSH     ALLOW    Anywhere
```

```console Termius · lms-server
$ sudo apt update && sudo apt upgrade -y

$ sudo fallocate -l 2G /swapfile
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
$ sudo swapon /swapfile
$ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
$ free -h
```

```plain ~/.ssh/config (WSL-ში)
Host lms
    HostName 164.90.12.34
    User giorgi
    IdentityFile ~/.ssh/id_ed25519
```

ფაილის სახელი `00-` იწყება, რადგან SSH ერთ პარამეტრზე **პირველ** ნანახ მნიშვნელობას იღებს, ფაილებს კი ანბანით კითხულობს — `00` ყველაზე ადრე იკითხება.
