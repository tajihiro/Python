org_str = '178'
KEY_VAL = 10000

print('初期値：', org_str)

enc_str = hex(int(org_str) + KEY_VAL)
print('暗号化：', enc_str)

print('生成中：', int(enc_str, 16))

dec_str = (int(enc_str, 16) - KEY_VAL)
print('復号化：', dec_str)
