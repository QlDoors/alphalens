import pandas as pd


def test_stack_and_unstack():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }, index=['X', 'Y', 'Z'])
    print(f'df:\n{df}')
    stacked = df.stack()
    print(f'stacked:\n{stacked}')
    unstacked = stacked.unstack()
    print(f'unstacked:\n{unstacked}')