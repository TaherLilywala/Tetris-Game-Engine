# Midsem Script
echo "1.3 --> $(grep ".*r'.*'.*" lexer.py | grep -cv "n+")"
echo "1.5 --> $(grep -c "\*\|d+" lexer.py)"
echo "1.6 --> $(grep -c "r'[A-Z].*" lexer.py)"