for i in range(160, 201):
    print(f"""
    def name(self):
        self.assertTrue(TestLexer.checkLexeme(
            "", "", {i}))""")
