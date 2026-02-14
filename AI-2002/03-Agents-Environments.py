from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import random

class Status(Enum):
    SAFE = "safe"
    VULNERABLE = "vulnerable"

@dataclass
class Component:
    name: str
    status: Status

class Environment:
    def __init__(self) -> None:
        names = ['A', 'B', 'C', 'D','E','F','G','H','I']
        self.components: List[Component] = [
            Component(
                name=name,
                status=random.choice([Status.SAFE, Status.VULNERABLE])
            )
            for name in names
        ]
    
    def get_percept(self, component: Component) -> Status:
        return component.status

    def patch_component(self, component: Component):
        component.status = Status.SAFE

    def display_state(self):
        for component in self.components:
            print(f"{component.name}: {component.status.value}")

class SecurityAgent:
    def __init__(self):
        self.vulnerable_list: List[Component] = []

    def scan(self, component: Component, percept: Status):
        if percept == Status.VULNERABLE:
            print(f"[VULNERABE] {component.name}")
            self.vulnerable_list.append(component)
        else:
            print(f"[SAFE] {component.name}")

    def patch(self, environment: Environment):
        for component in self.vulnerable_list:
            environment.patch_component(component)
        self.vulnerable_list.clear()

def T1():
    env = Environment()
    agent = SecurityAgent()

    print("====Intitial State====")
    env.display_state()

    print("====System Scan====")
    for component in env.components:
        percept = env.get_percept(component)
        agent.scan(component, percept)

    print("====Patch====")
    agent.patch(env)

    print("====Final State====")
    env.display_state()


class LoadStatus(Enum):
    UNDERLOADED = "Underloaded"
    BALANCED = "Balanced"
    OVERLOADED = "Overloaded"

@dataclass
class Server:
    name: str
    status: LoadStatus

class Environment:
    def __init__(self) -> None:
        server_names = ['Pehla', 'Dusra', 'Teesra', 'Chauhta', 'Panchwa']
        self.servers: List[Server] = [
            Server(name=name, status=random.choice(list(LoadStatus)))
            for name in server_names
        ]

    def get_percept(self, server: Server) -> LoadStatus:
        return server.status

    def update_status(self, server: Server, new_status: LoadStatus):
        server.status = new_status

    def display_state(self):
        for server in self.servers:
            print(f"{server.name}: {server.status.value}")

class LoadBalancerAgent:
    def __init__(self):
        self.overloaded_list: List[Server] = []
        self.underloaded_list: List[Server] = []

    def scan(self, server: Server, percept: LoadStatus):
        if percept == LoadStatus.OVERLOADED:
            print(f"[OVERLOADED] {server.name}")
            self.overloaded_list.append(server)
        elif percept == LoadStatus.UNDERLOADED:
            print(f"[UNDERLOADED] {server.name}")
            self.underloaded_list.append(server)
        else:
            print(f"[OK] {server.name}")

    def balance_load(self, environment: Environment):
        while self.overloaded_list and self.underloaded_list:
            overloaded = self.overloaded_list.pop()
            underloaded = self.underloaded_list.pop()

            print(f"Moving tasks from {overloaded.name} to {underloaded.name}...")

            environment.update_status(overloaded, LoadStatus.BALANCED)
            environment.update_status(underloaded, LoadStatus.BALANCED)

def T2():
    environment = Environment()
    agent = LoadBalancerAgent()

    print("===== INITIAL STATUS =====")
    environment.display_state()

    print("===== SCAN =====")
    for component in environment.servers:
        percept = environment.get_percept(component)
        agent.scan(component, percept)

    print("===== BALANCE LOAD =====")
    agent.balance_load(environment)

    print("===== FINAL STATUS =====")
    environment.display_state()

class BackupStatus(Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"

@dataclass
class Backup:
    name: str
    status: BackupStatus

class Environment:
    def __init__(self) -> None:
        backup_names = ['Pehla', 'Dusra', 'Teesra', 'Chauhta', 'Panchwa']
        self.backups: List[Backup] = [
            Backup(name=name, status=random.choice(list(BackupStatus)))
            for name in backup_names
        ]

    def get_status(self, backup: Backup) -> BackupStatus:
        return backup.status

    def update_status(self, backup: Backup, new_status: BackupStatus) -> None:
        backup.status = new_status

    def display_state(self) -> None:
        for backup in self.backups:
            print(f"{backup.name}: {backup.status.value}")

class BackupAgent:
    def __init__(self) -> None:
        self.failed_list: List[Backup] = []

    def scan(self, backup: Backup, status: BackupStatus) -> None:
        if status == BackupStatus.FAILED:
            print(f"[FAILED] {backup.name}")
            self.failed_list.append(backup)
        else:
            print(f"[OK] {backup.name}")

    def retry_failed(self, environment: Environment) -> None:
        for backup in self.failed_list:
            print(f"Retrying {backup.name}...")
            environment.update_status(backup, BackupStatus.COMPLETED)
            print(f"{backup.name} is now Completed.")
        self.failed_list.clear()

def T3() -> None:
    environment = Environment()
    agent = BackupAgent()

    print("===== INITIAL STATUS =====")
    environment.display_state()

    print("===== SCAN =====")
    for backup in environment.backups:
        agent.scan(backup, environment.get_status(backup))

    print("===== RETRY FAILED =====")
    agent.retry_failed(environment)

    print("===== FINAL STATUS =====")
    environment.display_state()

class ComponentStatus(Enum):
    SAFE = "Safe"
    LOW_RISK = "Low Risk"
    HIGH_RISK = "High Risk"

@dataclass
class Component:
    name: str
    status: ComponentStatus

class Environment:
    def __init__(self) -> None:
        component_names = ['A','B','C','D','E','F','G','H','I']
        self.components: List[Component] = [
            Component(name=name, status=random.choice(list(ComponentStatus)))
            for name in component_names
        ]

    def get_status(self, component: Component) -> ComponentStatus:
        return component.status

    def patch_component(self, component: Component) -> None:
        component.status = ComponentStatus.SAFE

    def display_state(self) -> None:
        for comp in self.components:
            print(f"Component {comp.name}: {comp.status.value}")

class SecurityAgent:

    def scan_and_patch(self, environment: Environment) -> None:
        print("\n===== SYSTEM SCAN =====")
        for comp in environment.components:
            status = environment.get_status(comp)
            if status == ComponentStatus.SAFE:
                print(f"[OK] Component {comp.name} is Safe.")
            elif status == ComponentStatus.LOW_RISK:
                print(f"[Low Risk] {comp.name}")
                print(f"Patching {comp.name}...")
                environment.patch_component(comp)
                print(f"{comp.name} patched")
            elif status == ComponentStatus.HIGH_RISK:
                print(f"[HIGH RISK] {comp.name}")
                print("Premium Service required")

def T4() -> None:
    environment = Environment()
    agent = SecurityAgent()

    print("===== INITIAL SYSTEM CHECK =====")
    environment.display_state()

    agent.scan_and_patch(environment)

    print("\n===== FINAL SYSTEM CHECK =====")
    environment.display_state()

@dataclass
class HospitalEnvironment:
    locations = []
    delivery_schedule = {}
    patient_ids = {}
    staff_available = True

    def __post_init__(self):
        self.locations = ['Medicine Storage', 'Corridor', 'Room101', 'Room102', 'Nurse Station']
        self.delivery_schedule = {
            'Room101': 'Paracetamol',
            'Room102': 'Antibiotic'
        }
        self.patient_ids = {
            'Room101': 'P101',
            'Room102': 'P102'
        }

    def get_schedule(self):
        return self.delivery_schedule

    def get_patient_id(self, room: str):
        return self.patient_ids[room]


@dataclass
class DeliveryRobot:
    goal = "Deliver Medicine"
    current_location = "Corridor"
    carrying_medicine= None

    def move(self, location: str) -> None:
        self.current_location = location
        print(f"Robot moved to {location}")

    def pick_medicine(self, medicine: str) -> None:
        self.carrying_medicine = medicine
        print(f"Picked up {medicine}")

    def scan_patient_id(self, patient_id: str) -> None:
        print(f"Scanned Patient ID: {patient_id}")

    def deliver_medicine(self, room: str) -> None:
        print(f"Delivered {self.carrying_medicine} to {room}")
        self.carrying_medicine = None

    def alert_staff(self) -> None:
        print("Alerting staff for assistance!")

    def execute_goal(self, environment: HospitalEnvironment) -> None:
        schedule = environment.get_schedule()
        for room, medicine in schedule.items():
            self.move("Medicine Storage")
            self.pick_medicine(medicine)
            self.move(room)
            patient_id = environment.get_patient_id(room)
            self.scan_patient_id(patient_id)
            self.deliver_medicine(room)


def T5() -> None:
    environment = HospitalEnvironment()
    robot = DeliveryRobot()

    print("===== DELIVERY STARTED =====")
    robot.execute_goal(environment)
    print("===== DELIVERY COMPLETED =====")


class RoomStatus(Enum):
    SAFE = "Safe"
    FIRE = "Fire"

@dataclass
class FireEnvironment:
    rooms = {}
    
    def __post_init__(self):
        self.rooms = {
            'a': RoomStatus.SAFE,
            'b': RoomStatus.SAFE,
            'c': RoomStatus.FIRE,
            'd': RoomStatus.SAFE,
            'e': RoomStatus.FIRE,
            'f': RoomStatus.SAFE,
            'g': RoomStatus.SAFE,
            'h': RoomStatus.SAFE,
            'j': RoomStatus.FIRE
        }

    def get_status(self, room):
        return self.rooms[room]

    def extinguish_fire(self, room):
        self.rooms[room] = RoomStatus.SAFE

    def display_environment(self, robot_position):
        grid_order = ['a','b','c','d','e','f','g','h','j']
        display = []
        for room in grid_order:
            if room == robot_position:
                display.append("R")
            elif self.rooms[room] == RoomStatus.FIRE:
                display.append("F")
            else:
                display.append(" ")
        for i in range(0, 9, 3):
            print(" | ".join(display[i:i+3]))

@dataclass
class FirefightingRobot:
    path = ['a','b','c','d','e','f','g','h','j']
    current_location = None

    def move(self, location: str):
        self.current_location = location
        print(f"\nRobot moved to room '{location}'")

    def detect_and_extinguish(self, environment: FireEnvironment):
        if environment.get_status(self.current_location) == RoomStatus.FIRE:
            print("Fire detected! Extinguishing fire...")
            environment.extinguish_fire(self.current_location)
            print("Fire extinguished.")
        else:
            print("No fire detected.")

    def execute_mission(self, environment: FireEnvironment):
        for room in self.path:
            self.move(room)
            self.detect_and_extinguish(environment)
            environment.display_environment(room)

def T6():
    environment = FireEnvironment()
    robot = FirefightingRobot()

    print("===== SIMULATION  =====")
    robot.execute_mission(environment)
    environment.display_environment(None)


if __name__ == "__main__":
    T6()