# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def is_rule_30(input_lists, rule_30_table):
    # Checks to see if rule 30 tables are the same
    if input_lists == rule_30_table:
        return "True"
    else:
        return "False"

if __name__ == '__main__':
    # Test 1 - positive result
    input_lists = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
        ["True", "True", "True", "False"]
        ]
    rule_30_table = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
        ["True", "True", "True", "False"]
    ]
    actual = is_rule_30(input_lists, rule_30_table)
    expected = "True"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    input_lists = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
        ["True", "True", "True", "True"]
    ]
    rule_30_table = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
        ["True", "True", "True", "False"]
    ]
    actual = is_rule_30(input_lists, rule_30_table)
    expected = "True"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    input_lists = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
    ]
    rule_30_table = [
        ["False", "False", "False", "False"],
        ["False", "False", "True", "True"],
        ["False", "True", "False", "True"],
        ["False", "True", "True", "True"],
        ["True", "False", "False", "True"],
        ["True", "False", "True", "False"],
        ["True", "True", "False", "False"],
        ["True", "True", "True", "False"]
    ]
    actual = is_rule_30(input_lists, rule_30_table)
    expected = "True"
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
