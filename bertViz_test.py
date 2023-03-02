# -*- coding:utf-8 -*-

from bertviz.transformers_neuron_view import GPT2Model, GPT2Tokenizer
from bertviz.neuron_view import show
from transformers import BertTokenizer
#from transformers.modeling_gpt2 import GPT2PreTrainedModel, GPT2Model

model_type = 'gpt2'
model_version = 'gpt2'
model = GPT2Model.from_pretrained("output_dir/checkpoint-139805")
tokenizer = BertTokenizer.from_pretrained("vocab/vocab.txt", do_lower_case=True)
text = "体育馆中，王珊对陈晓明说：「我让你十分，你也赢不了我」"


show(model, model_type, tokenizer, text, display_mode="light")