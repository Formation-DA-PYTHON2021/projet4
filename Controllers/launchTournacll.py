from ..Views.launchTournaview import ViewLaunchTournament
from ..Models.launchTournamdl import LaunchTournament


class ControllerLaunchTournament:
    def __init__(self):
        self.view = ViewLaunchTournament()

    def __call__(self):
        launchTourna = self.view.info()
        print(*launchTourna)
        launchTourna1 = LaunchTournament(*launchTourna)
        return LaunchTournament.update(launchTourna1)