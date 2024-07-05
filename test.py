'''
This file is used to test the compatibility of the model
with AutoClasses.
'''

from transformers import AutoConfig, AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("khrisintw/merge1")
tokenizer = AutoTokenizer.from_pretrained("khrisintw/merge1")