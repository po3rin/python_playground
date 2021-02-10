import torch
from transformers import BertJapaneseTokenizer, BertForMaskedLM

# Load pre-trained tokenizer
tokenizer = BertJapaneseTokenizer.from_pretrained(
    'cl-tohoku/bert-base-japanese-whole-word-masking')

# Tokenize input
text = '膝がとても痛いので会社を休みます。'
tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)
# ['テレビ', 'で', 'サッカー', 'の', '試合', 'を', '見る', '。']

# Mask a token that we will try to predict back with `BertForMaskedLM`
# masked_index = 0
# tokenized_text[masked_index] = '[CLS]'
masked_index = 6
tokenized_text[masked_index] = '[MASK]'
# masked_index = 12
# tokenized_text[masked_index] = '[SEP]'
print(tokenized_text)
# ['テレビ', 'で', '[MASK]', 'の', '試合', 'を', '見る', '。']

# Convert token to vocabulary indices
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
# [571, 12, 4, 5, 608, 11, 2867, 8]

# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor([indexed_tokens])
# tensor([[ 571,   12,    4,    5,  608,   11, 2867,    8]])

# Load pre-trained model
model = BertForMaskedLM.from_pretrained(
    'cl-tohoku/bert-base-japanese-whole-word-masking')
model.eval()

# Predict
with torch.no_grad():
    outputs = model(tokens_tensor)
    predictions = outputs[0][0, masked_index].topk(10)  # 予測結果の上位5件を抽出

# Show results
for i, index_t in enumerate(predictions.indices):
    index = index_t.item()
    token = tokenizer.convert_ids_to_tokens([index])[0]
    print(i, token)
