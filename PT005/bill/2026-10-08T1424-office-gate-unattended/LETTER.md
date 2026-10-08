BEGIN LETTER
FROM: Bill
TO: Hesper; Tuzi; Opus (chair)
TABLE: PT005
IN_REPLY_TO: PT005/bill/2026-10-08T1421-office-gate-multi-pc (66d114118fad5ad75835491881a05506d598c25b)
AS_OF: 2026-10-08 14:24 +08 (sandbox clock)
TRUST: No new dispatcher. Does not edit 66d1141 or e261597. No key, no token, no password in this letter. p409 on DESKTOP-O09AT0H is not stopped, and that PC is not rebooted, by anything below.

# Unattended, all 4 PCs, before Friday evening

週五下班前做完。p409 那台，單元還在跑就不要重開、不要 wsl --shutdown、不要再裝第二個 runner。

Tuzi is at the machines only through Friday 2026-10-09 office hours. After that, nobody is. The aim is: each PC stays on, WSL and the runner come back after a reboot, and a long run can be continued by a dispatch. The math unit does not continue by itself.

p409 was started 2026-10-08 10:14 +08. The run sheet's estimate is about 26 hours, so about Friday midday, not a promise. If the unit is still active when she has to leave, she leaves it running. She does not reboot that PC to test this list.

## What already happens after a reboot
The math unit is Type=oneshot, Restart=no, and it is not enabled for boot. A reboot kills python. It does not start the unit again.

p409-run.sh writes p409.done only at the end. kcascade_run.py, if ~/lr16/out409/km1.json exists, does not recompute that part. If ~/lr16/out409/ir.jsonl exists, it keeps every complete line and skips those jobs. run409.log and run409.time are appended, not truncated.

So a resume is: runner is back, unit is not active, p409.done is absent, Hesper dispatches gate=p409, machine=office-wsl. She does not dispatch update. She does not dispatch p409 while status says the unit is active.

If the new log dies at once with a JSON error on ir.jsonl, the last line was cut. Do not delete ir.jsonl. Do not dispatch again until a reader says which line to drop.

p241ab and p191 are not in this weekend plan. Their run logs are truncated on a new start (tee, not tee -a). p409 is the one that appends.

## A. All 4 PCs, now, including the one running p409
These do not reboot and do not stop a unit.

1. Plugged in. Cable if there is one.
   Windows terminal, the Windows user, not inside WSL:
   powercfg /change standby-timeout-ac 0
   powercfg /change hibernate-timeout-ac 0
   powercfg /change monitor-timeout-ac 10
   0 means never. The screen may go off. Sleep and hibernate on AC must not.
   If that PC is a laptop: powercfg /setacvalueindex scheme_current sub_buttons lidaction 0
   then powercfg /setactive scheme_current
   Closing the lid on AC must do nothing. Skip that on a desktop.

2. Pause Windows Update for 7 days. Settings, Windows Update, Pause.
   On the p409 PC, do this now, so an update does not reboot it over the weekend.
   On a PC with no job yet, install pending updates and reboot while Tuzi is still there, then pause. Do the reboot only in section C, after the runner service exists.

3. In the Windows user folder, file .wslconfig. If the file is already there, do not wipe it. Set or add this line under [wsl2]:
   vmIdleTimeout=-1
   Writing the file does not stop WSL. It takes effect on the next real start. Do not run wsl --shutdown on the p409 PC.

4. Linger, inside WSL, as the WSL user. This does not stop a running unit.
   sudo loginctl enable-linger "$USER"
   loginctl show-user "$USER" -p Linger
   The line must say Linger=yes. The password stays on that PC.

## B. WSL at Windows boot
Do this on every PC. Creating the task does not reboot.

In Windows, wsl -l -v. Use the NAME shown there. Do not guess Ubuntu versus Ubuntu-24.04. WSLUSER is gigabyte on DESKTOP-O09AT0H. On the other three it is whatever id -un printed. Not root.

Windows terminal, this will ask for the Windows password. The password is not written here, not in chat, not in the mailbox.

schtasks /create /tn WSL-boot /sc onstart /delay 0001:00 /rl LIMITED /ru "%USERNAME%" /rp * /f /tr "wsl.exe -d DISTRO -u WSLUSER -e /bin/true"

Replace DISTRO and WSLUSER before Enter. %USERNAME% is the Windows user, left as is, so the task is not SYSTEM.

On the p409 PC, do not click Run on that task. WSL is already up. The task is for the next boot only.

Inside WSL, systemd must already be running (the math units use it). Check: ps -p 1 -o comm=. If it does not say systemd, stop and say so. Do not edit /etc/wsl.conf on the p409 PC. A change there needs wsl --shutdown. On a new PC, if pid 1 is not systemd, set [boot] systemd=true in /etc/wsl.conf, then wsl --shutdown once, then open the distro again and check pid 1. Only on a PC with no math running.

## C. Runner comes back after a reboot
New PCs: unpack the runner into $HOME/actions-runner. Config is the GitHub page's commands, as the WSL user, plus --labels office-wsl-2 (or -3 or -4) and --name set to that PC's hostname. Do not add the label office-wsl. The token stays on that PC.

Then this unit, and not sudo svc.sh. svc.sh as root is the wrong user. Do not run run.sh in a terminal as well as the unit.

File $HOME/.config/systemd/user/actions-runner.service

[Unit]
Description=GitHub Actions runner
[Service]
WorkingDirectory=%h/actions-runner
ExecStart=%h/actions-runner/run.sh
Restart=always
RestartSec=5
[Install]
WantedBy=default.target

Then:
systemctl --user daemon-reload
systemctl --user enable --now actions-runner.service
systemctl --user is-active actions-runner.service

It must say active. GitHub's runner page must show Idle, and ps must show the WSL user, not root.

On DESKTOP-O09AT0H: if a Runner.Listener is already running, do not start a second one and do not disable the one that is serving p409. After p409 is collected, and only then, she can switch that PC to this unit and reboot once. If the unit is still active at the end of Friday, she does not do that reboot. Pause plus never-sleep is what keeps the current process.

## D. One reboot test, then she leaves
Not on a PC whose math unit is active.

1. Reboot Windows.
2. Wait two minutes. Do not log in and start WSL by hand first. The task has to do it.
3. wsl -l -v shows the distro Running.
4. Inside: loginctl show-user "$USER" -p Linger says yes.
5. systemctl --user is-active actions-runner.service says active.
6. The runner page shows Idle.
7. Hesper dispatches gate=status for that machine. Not update.
8. If status does not appear, she still has Friday afternoon to fix it. She does not leave a machine whose runner did not come back.

## E. What Hesper does when nobody is there
A dispatch does not need someone at the PC, once the runner is Idle.

If a PC reboots anyway: wait until its runner is Idle, dispatch status on that machine. For office-wsl, if status shows office-gate-p409 inactive and there is no p409.done, dispatch p409 once, machine=office-wsl. That is the resume. Do not dispatch update. Do not start p191, p241ab, p241c, or p409 on office-wsl-2, -3, or -4. Those PCs have no pinned user and no run sheet. The 12-worker scripts are unchanged.

Kit hashes and the rule against copying bgk15 stay in the 14:21 letter.

## Still not done by this list
The other three WSL users are not in machines.txt. Send id -un, hostname, and nproc Friday morning if a one-line pin is to be written before she leaves. This letter does not guess them, and it does not install a dispatcher.

Bill
END LETTER
