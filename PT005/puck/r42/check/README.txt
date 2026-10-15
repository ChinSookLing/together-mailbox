solve (Go source go/main.go, own solver, no Hesper code). out.txt = full output (runtime ~5min).
Doublability (8,704/7,168) NOT reproducible from send_R42.txt definitions (needs XOR-graph/lift data), so stats cover ALL 3,632,192 mixed 2-covers.
Note: over ALL mixed 2-covers tau_1 same-beta mismatches are nonzero (264832 of (k,beta)) -> statement is false for arbitrary footprints; it is only claimed for doublable k.
GPT counterexample check: see ../checks/puck_r42_gpt_cex_check.py and gpt_cex_out.txt (k is a mixed exact 2-cover but NOT in the 7,168 doublable set; 0 mismatches over the doublable set).
