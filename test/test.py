import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1

    # Start transfer
    dut.ui_in.value = 8'hA5

    await ClockCycles(dut.clk, 2)

    # BUSY bit is uo_out[0]
    assert int(dut.uo_out.value) != 0

    await ClockCycles(dut.clk, 20)
