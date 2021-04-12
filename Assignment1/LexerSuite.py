import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
#
#test comment
    def test_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**anhtaideptrai""","""Unterminated Comment""",101))
    def testcase_normal_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**Normal comment**","<EOF>",139))
    def testcase_multi_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**Multiline comment\nLine1\nLine2**","<EOF>",140))
    def test_five_stars(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",102))
    def test_multi_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**anhtaideptrai
        line1
        *line2
        * * line3
        ** ""","""<EOF>""",103))
    def test_comment_simple(self):
        self.assertTrue(TestLexer.checkLexeme("**this is *a comment**","<EOF>",120))
    def test_unterminated_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("**this is *a comment not close * * * * *","Unterminated Comment",127))
    def test_comment_star(self):
        self.assertTrue(TestLexer.checkLexeme("*** ** *****","*,<EOF>",135))
    def test_unterminated_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("***this is *a comment not close *\*\*\*","Unterminated Comment",138))
    def test_unterminated_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("***this is *a comment not %$@$@#%%#$@#$% *\*\*\*","Unterminated Comment",141))




#test ID:
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",104))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",105))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",106))
    def test_wrong_open_token(self):
        self.assertTrue(TestLexer.checkLexeme("a = Be*2;","a,=,Error Token B",112))
    def test_identifier_int(self):
        self.assertTrue(TestLexer.checkLexeme("01ancmds abc_ 12mckm","0,1,ancmds,abc_,12,mckm,<EOF>",121))
    def test_identifier_float(self):
        self.assertTrue(TestLexer.checkLexeme("4.9abc a95 7bc","4.9,abc,a95,7,bc,<EOF>",122))
    def test_identifier_string(self):
        self.assertTrue(TestLexer.checkLexeme("""  4.9"ab"ba a95 7bc""","4.9,ab,ba,a95,7,bc,<EOF>",123))
    def test_identifier_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("""  ab Function baBody""","ab,Function,baBody,<EOF>",124))
    def test_identifier_operator(self):
        self.assertTrue(TestLexer.checkLexeme("""  ab++45cd-- t\\u4""","ab,+,+,45,cd,-,-,t,\,u4,<EOF>",125))
    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme("1taideptr@ai","1,taideptr,Error Token @",131))
    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("1taideptr$$%^ai","1,taideptr,Error Token $",132))

#test literal
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""500 60 ab9""","500,60,ab9,<EOF>",107))
    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""9000asd943598gdjf89345978ssdfu374523shjf7isyf8345""","9000,asd943598gdjf89345978ssdfu374523shjf7isyf8345,<EOF>",153))
    def test_integer2(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""588 3476 0x54345 0X457AEfd""","588,3476,0x54345,0X457AE,fd,<EOF>",154))
    def test_integer3(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""0X457FZ""","0X457F,Error Token Z",155))
    def test_integer4(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""0000X457FZ""","0,0,0,0X457F,Error Token Z",156))
    def test_integer5(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""0o00X457FZ""","0,o00X457FZ,<EOF>",157))
    def test_integer6(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""0 199 0xFF 0XABC""","0,199,0xFF,0XABC,<EOF>",158))
    def test_integer7(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""0o567 0O77""","0o567,0O77,<EOF>",159))
    def test_integer8(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("""500 60 ab9""","500,60,ab9,<EOF>",108))
    def test_float(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("120.300      120.    300.e-30","120.300,120.,300.e-30,<EOF>",160))
    def test_float1(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5","12.0e3,12,e3,12.e5,<EOF>",161))
    def test_float2(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12000. 120000e-1","12.0e3,12000.,120000,e,-,1,<EOF>",162))
    def test_float3(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("12.0XABCDEF","12.0XABCDEF,<EOF>",163))
    def test_float4(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("400.400.e2763.45","400.400,.,e2763,.,45,<EOF>",164))
    def test_float5(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("500 400 . 34","500,400,.,34,<EOF>",165))
    def test_float6(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("0x46ABCD.455","0x46ABCD.455,<EOF>",166))
    def test_array(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("{1,    2}   {4,5  }   {  3  ,5}","{,1,,,2,},{,4,,,5,},{,3,,,5,},<EOF>",109))
    def test_array_2chieu(self):
        """test array 2chieu"""
        self.assertTrue(TestLexer.checkLexeme("{{1,    2},{4,5  },{  3  ,5}}","{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},<EOF>",110))
    def test_array_3chieu(self):
        """test array 3chieu"""
        self.assertTrue(TestLexer.checkLexeme("{{{1,    2},{4,5  },{  3  ,5}},{{1,    2},{4,5  },{  3  ,5}}}","{,{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},,,{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},},<EOF>",111))
    def test_float_with_000expo(self):
        self.assertTrue(TestLexer.checkLexeme("  12.000e3 ","""12.0,0,0,e3,<EOF>""",118))
    def test_int_and_float(self):
        self.assertTrue(TestLexer.checkLexeme("  12.000e3 23e4 23.e4 23  e4 ","""12.0,0,0,e3,23,e4,23.e4,23,e4,<EOF>""",128))
    def test_bool(self):
        self.assertTrue(TestLexer.checkLexeme("  e4True 2False 2.True ","""e4True,2,False,2.,True,<EOF>""",129))
    def test_bool_with_string(self):
        self.assertTrue(TestLexer.checkLexeme("""  4True"True hay False" ""","""4,True,True hay False,<EOF>""",130))
    def test_lit1(self):
        self.assertTrue(TestLexer.checkLexeme("""  4True"True hay False" ""","""4,True,True hay False,<EOF>""",130))
    def test_lit2(self):
        self.assertTrue(TestLexer.checkLexeme("""  {"anhtai",34.e5,0x45FA} ""","""{,anhtai,,,34.e5,,,0x45FA,},<EOF>""",172))
    def test_lit3(self):
        self.assertTrue(TestLexer.checkLexeme("""  {{"anhtai",34.e5,0x45FA},{}} ""","""{,{,anhtai,,,34.e5,,,0x45FA,},,,{,},},<EOF>""",179))
    def test_lit4(self):
        self.assertTrue(TestLexer.checkLexeme("""  {"anhtai",34.e5,0x45FA},{4\\.2&&3} ""","""{,anhtai,,,34.e5,,,0x45FA,},,,{,4,\.,2,&&,3,},<EOF>""",180))
    def test_lit5(self):
        self.assertTrue(TestLexer.checkLexeme("""  {} ""","""{,},<EOF>""",181))

#test string
    def test_normal_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This simple string"  ""","""This simple string,<EOF>""",134))
    def test_normal_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "I\\'m HCMUT Student\\t \\n"  ""","""I\\'m HCMUT Student\\t \\n,<EOF>""",133))
    def test_illegal_escape_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",113))
    def test_illegal_escape_2(self):
        """test illegal escape_2"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc' def"  ""","""Illegal Escape In String: abc' """,114))
    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,115))
    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",116))
    def test_string_end_with_escape_quote(self):
        """test_string_end_with_escape_quote"""
        self.assertTrue(TestLexer.checkLexeme("""  "bdef'"  ""","""Unclosed String: bdef'"  """,117))
    def test_string_with_newline(self):
        self.assertTrue(TestLexer.checkLexeme("""  "abcde\n asd" ""","""Unclosed String: abcde""",119))
    def test_string_uncloesd(self):
        self.assertTrue(TestLexer.checkLexeme("""  "abcde asd"" ""","""abcde asd,Unclosed String:  """,151))
    def test_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\h def"  ""","""abc\\\\h def,<EOF>""",152))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\ def"  ""","""Illegal Escape In String: abc\ """,167))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ def"  ""","""Illegal Escape In String: abc\ """,168))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\ def"  ""","""abc\\\\ def,<EOF>""",169))
    

#test expr
    def test_expression1(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("x = 6 --ab","x,=,6,-,-,ab,<EOF>",126))
    def test_expression2(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("ab=ab>=6.2","ab,=,ab,>=,6.2,<EOF>",136))
    def test_expression3(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("a<b*c*d<be46.2","a,<,b,*,c,*,d,<,be46,.,2,<EOF>",142))
    def test_expression4(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("x-465671263","x,-,465671263,<EOF>",143)) 
    def test_expression5(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("abc&abc\\56","abc,Error Token &",144))
    def test_expression6(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("a&&b&&g","a,&&,b,&&,g,<EOF>",145))
    def test_expression7(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("b=22-.456","b,=,22,-.,456,<EOF>",146))
    def test_expression8(self):
        """test_expression"""
        self.assertTrue(TestLexer.checkLexeme("c=56.7=/=34.e56","c,=,56.7,=/=,34.e56,<EOF>",147))

#test statements
    def test_statement1(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",148))
    def test_statement2(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x=6.7,t,y;","Var,:,x,=,6.7,,,t,,,y,;,<EOF>",149))
    def test_statement3(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x=6.7,t,y,;","Var,:,x,=,6.7,,,t,,,y,,,;,<EOF>",150))
    def test_statement4(self):
        self.assertTrue(TestLexer.checkLexeme("Varr: x=7;","Var,r,:,x,=,7,;,<EOF>",170))
    def test_function5(self):
        self.assertTrue(TestLexer.checkLexeme("While (i < 5) a[i] = b +. 1.0; i = i + 1; EndWhile.","While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;, EndWhile,.,<EOF>",171))    
    def test_statement6(self):
        self.assertTrue(TestLexer.checkLexeme("For (i = 0, i < 10, 2) Do writeln(i); EndFor.","For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>",173))
    def test_statement7(self):
        self.assertTrue(TestLexer.checkLexeme("Do statement-list While expression EndDo.","Do,statement,-,list,While,expression,EndDo,.,<EOF>",174))
    def test_statement8(self):
        self.assertTrue(TestLexer.checkLexeme("Break;","Break,;,<EOF>",175))
    def test_statement9(self):
        self.assertTrue(TestLexer.checkLexeme("Continue;","Continue,;,<EOF>",176))
    def test_statement10(self):
        self.assertTrue(TestLexer.checkLexeme("foo (2 + x, 4. \\. y); goo ();","foo,(,2,+,x,,,4.,\.,y,),;,goo,(,),;,<EOF>",177))
    def test_statement11(self):
        self.assertTrue(TestLexer.checkLexeme("Return foo (2 + x, 4. \\. y);","Return,foo,(,2,+,x,,,4.,\.,y,),;,<EOF>",178))
    def test_statement12(self):
        self.assertTrue(TestLexer.checkLexeme("Var: a[5] = {}; Var: b[2][3]={{1,2,3},{4,5,6}};","Var,:,a,[,5,],=,{,},;,Var,:,b,[,2,],[,3,],=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>",182))
    def test_statement13(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",183))
    def test_statement14(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",184))
    def test_statement15(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",185))
    def test_statement16(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",186))
    def test_statement17(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",187))
    def test_statement18(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",188))
    def test_statement19(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",189))
    def test_statement20(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",190))
    def test_statement21(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",191))
    def test_statement22(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",192))
    def test_statement23(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",193))
    def test_statement24(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",194))
    def test_statement25(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",195))
    def test_statement26(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",196))
    def test_statement27(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",197))
    def test_statement28(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",198))
    def test_statement29(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",199))
    def test_statement30(self):
        self.assertTrue(TestLexer.checkLexeme("If a>.6 Then b=89.5 EndIf.","If,a,>.,6,Then,b,=,89.5,EndIf,.,<EOF>",200))
    
