from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Protocol

class AgentStatus(Enum):
    ACTIVE = auto()
    INACTIVE = auto()

class can_perform(Protocol):
    def perform(self):
        ...

@dataclass
class SecurityAgent(ABC):
    idx: int
    name: str
    status: AgentStatus
    
    @abstractmethod
    def perform(self):
        pass

class FirewallAgent(SecurityAgent):
    def perform(self):
        self.monitor_traffic()

    def monitor_traffic(self):
        print("Monitoring Traffic...")

class MalwareAgent(SecurityAgent):
    def perform(self):
        self.scan_files()

    def scan_files(self):
        print("Scanning Files...")

class AutomationAgent(SecurityAgent):
    def perform(self):
        self.run_automation()

    def run_automation(self):
        print("Running Automation...")

def simulate(*agents: can_perform) -> None:
    for agent in agents:
        agent.perform()

def T1():
    simulate(
        FirewallAgent(0, "Qwen", AgentStatus.ACTIVE),
        MalwareAgent(1, "Clip", AgentStatus.ACTIVE),
        AutomationAgent(2, "MLLM", AgentStatus.INACTIVE)
    )

#######################################################
#                   Task 2
#######################################################
class Severity(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class can_perform(Protocol):
    def perform(self):
        ...

@dataclass
class Threat(ABC):
    threat_id: int
    name: str
    severity: Severity
    
    @abstractmethod
    def perform(self) -> None:
        ...

class PhishingThreat(Threat):
    def perform(self):
        self.analyze_emails()

    def analyze_emails(self):
        print("Analyzing emails...")

class RansomwareThreat(Threat):
    def perform(self):
        self.scan_files()

    def scan_files(self):
        print("Scanning Files...")

class BotnetThreat(Threat):
    def perform(self):
        self.detect_traffic()

    def detect_traffic(self):
        print("Monitoring Traffic...")

def simulate(*threats: can_perform):
    for threat in threats:
        threat.perform()

def T2():
    simulate(
        PhishingThreat(1, "faizan", Severity.HIGH),
        RansomwareThreat(2, "farooq", Severity.LOW),
        BotnetThreat(3, "shaheer", Severity.MEDIUM),
    )

#######################################################
#                   Task 3
#######################################################
class can_respond(Protocol):
    def execute_response(self) -> None:
        ...

@dataclass
class ResponseAgent(ABC):
    agent_id: int
    name: str

    @abstractmethod
    def execute_response(self) -> None:
        ...

class AlertAgent(ResponseAgent):
    def execute_response(self):
        self.send_notification()

    def send_notification(self):
        print("Sending security alerts...")

class BlockAgent(ResponseAgent):
    def execute_response(self):
        self.block_activity()

    def block_activity(self):
        print("Blocking malicious activities...")

class RecoverAgent(ResponseAgent):
    def execute_response(self):
        self.restore_systems()

    def restore_systems(self):
        print("Restoring affected systems...")

def respond(*agents: can_respond):
    for agent in agents:
        agent.execute_response()

def T3():
    respond(
        AlertAgent(1, "AlertBot"),
        BlockAgent(2, "BlockBot"),
        RecoverAgent(3, "RecoverBot"),
    )

#######################################################
#                   Task 4
#######################################################
class can_work(Protocol):
    def work(self) -> None:
        ...

@dataclass
class Employee(ABC):
    employee_id: int
    name: str

    @abstractmethod
    def work(self) -> None:
        ...

class Manager(Employee):
    def work(self):
        self.manage_team()

    def manage_team(self):
        print(f"{self.name} is managing the team...")

class Developer(Employee):
    def work(self):
        self.write_code()

    def write_code(self):
        print(f"{self.name} is writing code...")

class Designer(Employee):
    def work(self):
        self.create_designs()

    def create_designs(self):
        print(f"{self.name} is creating designs...")

def simulate_work(*employees: can_work):
    for employee in employees:
        employee.work()

def T4():
    simulate_work(
        Manager(1, "Aliyan"),
        Developer(2, "Mian"),
        Designer(3, "Khush"),
    )                   

#######################################################
#                   Task 5
#######################################################
class Grade(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()

@dataclass
class Student:
    name: str
    _grade: Grade

    # use same name
    @property
    def grade(self) -> Grade:
        return self._grade

    @grade.setter
    def grade(self, value: Grade):
        self._grade = value

    def display_info(self):
        print(f"{self.name}: {self._grade.name}")

def T5():
    student = Student("aliyan", Grade.A)
    student.display_info()
    student.grade = Grade.B # access like usual attribute
    student.display_info()

#######################################################
#                   main()
#######################################################
if __name__=="__main__":
    T5()
