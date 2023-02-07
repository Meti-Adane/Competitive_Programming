'''
        HELPER FUCNITONS
        function Justify_left:
            calculate remainig spaces i.e maxwidth - size
            add remaining spaces to end of line
        fucntion Justify:
            calculate remaining_space i.e maxwidth - size
            calculate padding_space i.e remaining_space // max(1, (number of elements in line -1))
            calculate extra_space i.e remaining_space % max(1, (number of elements in line -1))
            for word in line:
                if word not last word in line:
                    add padding_space number of space after word
                if there exists extra_space:
                    add extra_space number of spaces after word
                    subtract the size of extra_space by one 

        PACK WORDS
        While word in input:
            if curr arr is empty:
                add word to arr
            elif currarr has prev word and current word + one whitespace can fit:
                add whitespace + word
                increase size by 1 # space taken by white space 
            elif the curr arr cannot fit in the curr word:
                copy the current arr to container
                set arr to contain current word 
                set size = 0 
            increase size by the current word added to arr 
        If arr has elements:
            add arr to container

        JUSTIFY 
        if line is last line or has only one element:
            left justfiy line 
        else
            justify line
            
        '''
        ans = []
        lines = self.packwords(words, maxWidth)
        for i, val in enumerate(lines):
            newline = []
            line, size = val
            if i < len(lines)-1 and len(line) > 1:
               newline = self.justify(line, maxWidth-size)
            else:
                newline = self.leftJustify(line, maxWidth-size)
            ans.append("".join(newline))
        return ans
        

    def packwords(self, words, maxWidth):
        lines = []
        line, size = [], 0

        for word in words:
            if not line:
                line.append(word)
            elif len(word) + size + 1 <= maxWidth:
                line.append(' '+word)
                size += 1
            else:
                lines.append((line.copy(), size))
                line = [word]
                size = 0 
            size += len(word)
        if line:
            lines.append((line.copy(), size))
        return lines
   
    def leftJustify(self, line, remaining):
        newline = []
        newline.append("".join(line))
        newline.append(' '* remaining)
        return newline

    def justify(self, line, remaining):
        newline = []
        equalPadding = remaining // max(len(line)-1, 1)
        extra = remaining % max(len(line)-1, 1)
        for j, word in enumerate(line):
            newline.append(word)
            if j < len(line)-1:
                newline.append(' '* equalPadding)
            if extra:
                newline.append(' ')
                extra -= 1
        return newline