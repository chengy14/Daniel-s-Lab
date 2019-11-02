# fetch the target
cmd.fetch('2b88')
# Initialize mutation
cmd.wizard("mutagenesis")
cmd.do("refresh_wizard")

# lets mutate residue 6 to GLN
cmd.get_wizard().set_mode("GLN")
cmd.get_wizard().do_select("6/")

# Select the rotamer
cmd.frame(10)

# Apply the mutation
cmd.get_wizard().apply()