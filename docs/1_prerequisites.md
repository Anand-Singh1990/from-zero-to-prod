# Linux
ps aux --forest
ps → show running processes
a → processes from all users
u → show user-oriented details (CPU, memory, user, etc.)
x → include processes not attached to a terminal (background services)

ps -elf --forest
ps → process status
-e → every process on the system
-l → long format (low-level info: priorities, flags, nice value, etc.)
-f → full format (UID, PID, PPID, start time, full command)
--forest → better hierarchy

Output
UID →	User who owns the process
PID →	Process ID
PPID →	Parent process ID
PRI →	Kernel priority
NI →	Nice value (user-set priority)
VSZ →	Virtual memory size
RSS →	Physical memory used
STAT →	Process state (R, S, Z, etc.)
CMD →	Full command that started it


top/htop → Monitory(Process Monitor)


ss -tulpn
Shows network ports that are currently open and which programs are using them.
ss → socket statistics (modern replacement for netstat)
-t → TCP connections
-u → UDP connections
-l → listening ports only (servers)
-p → show the process using the port
-n → show numbers (no DNS or service-name lookup)

sudo systemctl status ssh
Shows the current status of the SSH service (running, stopped, failed, etc.).
sudo → run as administrator (needed for service info)
systemctl → control systemd services
status → show detailed service state
ssh → the SSH service (sometimes called sshd)


# Python
python3 -m venv venv (Created Virtual Environment)
source venv/bin/activate (Activates Virtual Environment)
pip install fastapi (Install packages(here, fastapi))

# Git
git init
git checkout -b dev
git commit -m "test"
git push

# Networking
ping google.com (Reach the host at the network level?)
nslookup google.com (Resolves the domain name to an IP address?)
curl http://example.com(CTalks to the actual application (HTTP server)?)
