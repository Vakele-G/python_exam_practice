from io import StringIO
import fundamentals as fun
import sys

class TestFunctions():
    
    def test_pseudo_range_function_exists(self):
        assert callable(getattr(fun, 'pseudo_range', None)), \
            "Function 'pseudo_range' is not defined"


    def test_pseudo_range_output(self): 
        test_cases = [
            (3, ['1', '2', '3']),
            (5, ['1', '2', '3', '4', '5']),
            (1, ['1']),
            (7, ['1', '2', '3', '4', '5', '6', '7']),
            (10, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        ]
        
        for n, expected_output in test_cases:
            captured_output = StringIO() 
            sys.stdout = captured_output 
            fun.pseudo_range(n) 
            sys.stdout = sys.__stdout__ 
            output = captured_output.getvalue().strip().split('\n') 
            assert output == expected_output, (
                f"Function 'pseudo_range({n})' does not produce the expected output. Expected {expected_output}, got {output}")


    def test_do_not_panic_returns_correctly(self): 
        test_cases = [
                (3, True),  
                (4, True),   
                (5, False),  
                (6, False),  
                (7, True),  
                (8, True),   
                (10, False), 
            ]

        for n, expected in test_cases:
            result = fun.do_not_panic(n)
            actual_sum = n * (n + 1) // 2
            assert result == expected, \
                f"Function 'do_not_panic({n})' should return {expected}. Sum is {actual_sum} which is {'even' if actual_sum % 2 == 0 else 'odd'}"
    

    def test_countdown_even_output(self):
        test_cases = [
            (10, ['10', '8', '6', '4', '2', '0']),
            (7, ['6', '4', '2', '0']),
            (5, ['4', '2', '0']),
            (8, ['8', '6', '4', '2', '0']),
            (0, ['0']),
            (1, ['0']),
            (15, ['14', '12', '10', '8', '6', '4', '2', '0'])
        ]

        for n, expected_output in test_cases:
            captured_output = StringIO()
            sys.stdout = captured_output
            fun.countdown_even(n)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip().split('\n')
            assert output == expected_output, \
                f"Function 'countdown_even({n})' does not print correctly. Expected {expected_output}, got {output}"


    def test_weak_password(self):
        assert fun.check_password("abc") == "Weak", \
            "Function 'check_password' does not return 'Weak' for short passwords"
        
        assert fun.check_password("12345") == "Weak", \
            "Function 'check_password' does not return 'Weak' for short passwords"
        
    
    def test_medium_password(self):
        assert fun.check_password("abc123") == "Medium", \
            "Function 'check_password' does not return 'Medium' for alphanumeric passwords"
        
        assert fun.check_password("password1") == "Medium", \
            "Function 'check_password' does not return 'Medium' for alphanumeric passwords"
        
    
    def test_strong_password(self):
        assert fun.check_password("abc123!") == "Strong", \
            "Function 'check_password' does not return 'Strong' for passwords with symbols"
        
        assert fun.check_password("P@ssw0rd#") == "Strong", \
            "Function 'check_password' does not return 'Strong' for passwords with symbols"
        
    
    def test_invalid_password(self):
        assert fun.check_password("") == "Invalid", \
            "Function 'check_password' does not return 'Invalid' for empty passwords"
        

    def test_reverse_words_function_exists(self):
        assert callable(getattr(fun, 'reverse_words', None)), \
            "Function 'reverse_words' is not defined"
        
    
    def test_reverse_words_output(self):
        assert fun.reverse_words("Hello World") == "World Hello", \
            "Function 'reverse_words' does not reverse words correctly"
        
        assert fun.reverse_words("  This   is  a test  ") == "test a is This", \
            "Function 'reverse_words' does not handle multiple spaces correctly"
        

    def test_reverse_words_single_word(self):
        assert fun.reverse_words("Python") == "Python", \
            "Function 'reverse_words' does not handle single word correctly"
        

    def test_reverse_words_empty_string(self):
        assert fun.reverse_words("") == "", \
            "Function 'reverse_words' does not handle empty string correctly"
