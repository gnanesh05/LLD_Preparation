from elevatorSystem import ElevatorSystem
import time
class Demo:
    @staticmethod
    def run():
        elevatorSystem = ElevatorSystem(3,2)
        time.sleep(3)
        elevatorSystem.request_elevator(0,3)
        time.sleep(2)
        elevatorSystem.request_elevator(1,3)
        time.sleep(2)
        elevatorSystem.request_elevator(0,4)
        time.sleep(2)
        elevatorSystem.request_elevator(4,2)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping system due to keyboard interrupt.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            elevatorSystem.stop_all()
            print("Elevator shutdown")


if __name__ =='__main__':
    Demo.run()