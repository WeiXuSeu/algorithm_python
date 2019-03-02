from singletonClass import singleton_inst


if __name__ == "__main__":
    inst1 = singleton_inst
    print id(inst1)
    inst2 = singleton_inst
    print id(inst2)
