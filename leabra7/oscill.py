"""Components for Inhibitatory Oscillations in Layers"""
import math

from typing import List

from leabra7 import specs as sp
from leabra7 import events as ev


class Oscill(ev.EventListenerMixin):
    """An object that updates the inhibition of layers according to sinusoidal
    oscillations."""

    def __init__(self,
                 name: str,
                 layer_names: List[str],
                 spec: sp.OscillSpec = None) -> None:
        """Initialize oscilation"""
        self.name = name
        self.layer_names = layer_names

        if spec is None:
            self._spec = sp.OscillSpec()
        else:
            self._spec = spec

        self.mid = self._spec.mid
        self.inhib = self.mid
        self.amps = self._spec.amps.copy()
        self.periods = self._spec.periods.copy()
        self.tot_per = sum(self.periods)
        self.int_cycle = 0

    def find_period(self) -> int:
        """Finds period of oscillation in cycle."""
        c = self.int_cycle
        for i in range(len(self.periods)):
            if c < self.periods[i]:
                return i
            c -= self.periods[i]
        self.int_cycle -= self.tot_per
        return self.find_period()

    def cycle(self) -> None:
        """Cycle of oscillation"""
        i = self.find_period()
        offset = sum(self.periods[0:i])
        self.inhib = self.mid + self.amps[i] * math.sin(
            (self.int_cycle - offset) / self.periods[i] * math.pi)

        self.int_cycle += 1

        if self.int_cycle >= self.tot_per:
            self.int_cycle -= self.tot_per

    def get_inhib(self) -> float:
        return self.inhib

    def handle(self, event: ev.Event) -> None:
        if isinstance(event, ev.Cycle):
            self.cycle()
