import capstone
import os

file_count = 728
filenames = [f"binary{i}" for i in range(file_count + 1)]
inst_start_addr = 0x001019 # here is the addr of xor instruction
inst_end_addr = 0x00101f


output = ""

# Setting up the capstone disassembly engine for 64-bit architecture
dis_engine = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)

for file in filenames:
  with open(file, 'rb') as fp:
    data = fp.read()[inst_start_addr:inst_end_addr]

    disassembly = dis_engine.disasm(data, 0)

    xor_val = None
    cmp_val = None
    for decoded in disassembly:
      inst = f"{decoded.mnemonic} {decoded.op_str}"
      inst = inst.strip()

      # xor dl, 0x16
      if 'xor' in inst:
        xor_val = int(inst.split()[-1].replace('0x', ''), 16)

      # cmp dl, 0x21
      elif 'cmp' in inst:
        cmp_val = int(inst.split()[-1].replace('0x', ''), 16)

      # If the instruction is not an xor or cmp then investigate it
      else:
        print(f"Weird Instruction: {inst} for binary: {file}")
        exit()

    assert xor_val is not None
    assert cmp_val is not None

    output += chr(cmp_val ^ xor_val)

print(output)

