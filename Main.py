import time
import Elevator
import ServoRazorMotor
import Dominoes
import Hotwheels
import Plane	

HammerServoPin = #any #type: ignore
HammerButtonPin = #any #type: ignore

ElevatorControlPins = #any #type: ignore
ElevatorEndstopPin = #any #type: ignore
ElevatorShockSensorPin = #any #type: ignore

DistanceEcho = #any #type: ignore
DistanceTrig = #any #type: ignore
CarSolenoid = #any #type: ignore

JoyInPin = #ADCChannel #type: ignore

DcMotorInA = #any #type:ignore
DcMotorInB = #any #type:ignore

PlaneRelay = #any #type: ignore



if input("start program? y/n\n") == "y":
    Plane.init(PlaneRelay)
    time.sleep(5)
    print("Starting in 5")
    time.sleep(5)
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Button has been hit!")
    time.sleep(0.5)
    print("Activating Elevator")
    Elevator.main(ElevatorControlPins,ElevatorEndstopPin, ElevatorShockSensorPin)
    print("Elevator Finished")
    time.sleep(0.5)
    print("Hotwheels Released")
    Hotwheels.main(DistanceEcho,DistanceTrig,CarSolenoid)
    print("Hotwheels Finished")
    time.sleep(0.5)
    #print("Launching Ball")
    #Launch.main(pins)
    #print("Ball landed")
    time.sleep(0.5)
    print("Dominoes Starting")
    Dominoes.main(DcMotorInA,DcMotorInB)
    print("Dominoes Finished")
    time.sleep(0.5)
    print("Launching Plane")
    Plane.main(PlaneRelay)
    print("Program Finished")
else:
    exit(1)
