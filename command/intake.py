from robotpy_toolkit_7407.command import SubsystemCommand
from subsystem import Intake

class DeployIntake(SubsystemCommand[Intake]):

    def initialize(self) -> None:
        if self.subsystem.deployed:
            self.subsystem.retract()
        else:
            self.subsystem.deploy()

    def execute(self) -> None:
        pass

    def isFinished(self) -> bool:
        pass

    def end(self, interrupted: bool) -> None:
        pass

