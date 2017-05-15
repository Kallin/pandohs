import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],index=pd.date_range('1/1/2000', periods=10))

print (df)