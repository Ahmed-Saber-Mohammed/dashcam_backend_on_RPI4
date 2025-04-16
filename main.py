import threading
import time
import record_ir
import api

if __name__ == '__main__':
    ir_thread = threading.Thread(target=record_ir.ir_monitor, daemon=True)
    flask_thread = threading.Thread(target=api.run_flask, daemon=True)

    ir_thread.start()
    flask_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🚦 Exiting main program.")
