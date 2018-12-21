"""Testing oscillations implimentation"""
from leabra7 import oscill as osc
from leabra7 import events as ev
from leabra7 import specs as sp

import pytest


def test_oscill_init():
    theta = osc.Oscill(
        "theta", ["lr1"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1], periods=[100]))
    theta = osc.Oscill(
        "theta", ["lr1"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1, 0.3], periods=[100, 200]))


def test_oscill_init_multiple_layers():
    theta = osc.Oscill(
        "theta", ["lr1", "lr2"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1], periods=[100]))
    theta = osc.Oscill(
        "theta", ["lr1", "lr2"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1, 0.3], periods=[100, 200]))


def test_oscill_init_default():
    theta = osc.Oscill("theta", ["lr1"])
    theta = osc.Oscill("theta", ["lr1", "lr2"])


def test_oscill_finds_period():
    theta = osc.Oscill(
        "theta", ["lr1"],
        spec=sp.OscillSpec(
            mid=0.5, amps=[0.1, 0.3, 0.4], periods=[100, 200, 300]))
    for i in range(600):
        theta.int_cycle = i
        j = i % 600
        if j < 100:
            assert theta.find_period() == 0
        elif j < 300:
            assert theta.find_period() == 1
        else:
            assert theta.find_period() == 2


def test_oscill_updates_cycle():
    theta = osc.Oscill(
        "theta", ["lr1"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1], periods=[100]))
    for i in range(200):
        j = i % 100
        assert theta.int_cycle == j
        theta.cycle()


def test_oscill_handles_cycle_event(mocker):
    theta = osc.Oscill(
        "theta", ["lr1"],
        spec=sp.OscillSpec(mid=0.5, amps=[0.1], periods=[100]))
    mocker.spy(theta, "cycle")
    theta.handle(ev.Cycle())
    theta.cycle.assert_called_once()
