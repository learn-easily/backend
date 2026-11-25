# სერვერის დაცვა

lms-server — მზადაა შემდეგი ლექციისთვის, Nginx-ისთვის

## მოთხოვნები

- `00-hardening.conf`: root და პაროლი აკრძალულია → `restart ssh` (ჯერ Termius-ის ახალ tab-ში შეამოწმეთ!)
- `ufw`: მხოლოდ `OpenSSH` → `enable`
- swap 2 GB (`/etc/fstab`-ითაც)
- WSL-ში `~/.ssh/config` → `ssh lms`
- `~/scripts/hello.sh` (`echo "გამარჯობა, $USER"`) → გასაშვები (`chmod`) → `./scripts/hello.sh`

## ✓ მზადაა, როცა

`sshd -T` — `no`/`no`, root-ის Host — `Permission denied`, `ufw status` — active, `free -h` — Swap 2.0Gi, `ssh lms` შედის, `hello.sh` ეშვება

## ⭐ ბონუსი

- `sudo grep Invalid /var/log/auth.log | wc -l` — რამდენჯერ სცადეს ბოტებმა შესვლა მას შემდეგ, რაც სერვერი შექმენით? (`wc -l` — ხაზების რაოდენობა)

## ამოხსნა

```console Termius · giorgi@lms-server !
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

```console Termius · giorgi@lms-server
$ sudo fallocate -l 2G /swapfile
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
$ sudo swapon /swapfile
$ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
$ free -h

$ mkdir -p ~/scripts
$ nano ~/scripts/hello.sh          # echo "გამარჯობა, $USER"
$ chmod +x ~/scripts/hello.sh      # ან: chmod 755
$ ~/scripts/hello.sh
გამარჯობა, giorgi
```

```plain ~/.ssh/config (WSL-ში)
Host lms
    HostName 164.90.12.34
    User giorgi
    IdentityFile ~/.ssh/id_ed25519
```

ფაილის სახელი `00-` იწყება, რადგან SSH ერთ პარამეტრზე **პირველ** ნანახ მნიშვნელობას იღებს, ფაილებს კი ანბანით კითხულობს — `00` ყველაზე ადრე იკითხება. `hello.sh` `chmod +x`-ის გარეშე `Permission denied`-ით ჩავარდებოდა — ფაილს გაშვების (`x`) უფლება სჭირდება.
