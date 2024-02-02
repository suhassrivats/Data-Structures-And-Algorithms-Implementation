class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index = expression.find('+')
        ans = [float(inf), expression]

        def evaluate_expression(exp):
            exp_res = exp.replace( '(', '*(' ).replace( ')', ')*' ).strip('*')
            return eval(exp_res)

        for l in range(plus_index):
            for r in range(plus_index+1, len(expression)):
                exp = f'{expression[:l]}({expression[l:plus_index]}+{expression[plus_index+1:r+1]}){expression[r+1:len(expression)]}'
                exp_res = evaluate_expression(exp)
                if ans[0] > exp_res:
                    ans = [exp_res, exp]

        return ans[1]