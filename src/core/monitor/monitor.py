import threading
import time
from typing import Callable

class Monitor:
    def __init__(self, trap_handler):
        self.trap_handler = trap_handler
        self._running = False
        self._monitor_thread = None
        self._callbacks = []
        self._lock = threading.Lock()

    def start_monitoring(self):
        if self._running:
            return
        self._running = True
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()

    def stop_monitoring(self):
        self._running = False
        if self._monitor_thread:
            self._monitor_thread.join()

    def _monitor_loop(self):
        while self._running:
            # Placeholder: here real packet capture and analysis would happen
            suspicious_detected = self._simulate_detection()
            if suspicious_detected:
                self.trap_handler.emit_event('suspicious_activity_detected')
            time.sleep(1)

    def _simulate_detection(self) -> bool:
        # For demo purposes, randomly flag suspicious activity
        import random
        return random.random() < 0.01  # 1% chance each second

    def register_callback(self, callback: Callable):
        with self._lock:
            self._callbacks.append(callback)

    def emit_alert(self, alert_msg: str):
        with self._lock:
            for cb in self._callbacks:
                try:
                    cb(alert_msg)
                except Exception:
                    pass
