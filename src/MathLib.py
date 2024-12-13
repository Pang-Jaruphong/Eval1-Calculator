class MathLib:

    @classmethod
    def execute(self, mathRequest):
        oper = mathRequest.get_oper()
        ope1 = mathRequest.get_ope1()
        ope2 = mathRequest.get_ope2()

        if(oper == 'add'):
            res = ope1 + ope2
            mathRequest.set_res(res)

        if(oper == 'div'):
            res = ope1 / ope2
            mathRequest.set_res(res)

        if(oper == 'mul'):
            res = ope1 * ope2
            mathRequest.set_res(res)

        if(oper == 'sub'):
            res = ope1 - ope2
            mathRequest.set_res(res)

        if(oper == 'root'):
            res = ope1 ** (1/ope2)
            mathRequest.set_res(res)

        if(oper == 'pow'):
            res = ope1 ** ope2
            mathRequest.set_res(res)
