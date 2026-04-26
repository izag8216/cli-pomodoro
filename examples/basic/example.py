#!/usr/bin/env python3
"""Basic example: start a work session and display progress."""

from cli_pomodoro.core import TimerMachine

def main():
    timer = TimerMachine(work_minutes=1)  # 1 min for demo
    timer.start_work()

    print("Work session started! Press Ctrl+C to stop.\n")

    try:
        while True:
            status = timer.get_status()

            if status["state"] == "idle":
                break

            remaining = status["remaining_seconds"]
            progress = status.get("progress_percent", 0)

            mm, ss = divmod(remaining, 60)
            bar_len = 30
            filled = int(bar_len * progress / 100)
            bar = "=" * filled + "-" * (bar_len - filled)

            print(f"\r[{bar}] {mm:02d}:{ss:02d} ({progress:.1f}%)", end="", flush=True)

            if status["is_complete"]:
                print("\n\nSession complete!")
                break

            import time
            time.sleep(0.5)

    except KeyboardInterrupt:
        timer.stop()
        print("\n\nStopped.")

if __name__ == "__main__":
    main()