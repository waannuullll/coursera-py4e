text = "X-DSPAM-Confidence:    0.8475";

ind = text.find('0')
text = text[ind:ind+6]
print(float(text))
