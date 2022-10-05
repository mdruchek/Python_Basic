def special_symbol(symbol):
    if symbol == ' ':
        return ' '
    if symbol == '.':
        return '-'
    if symbol == '(':
        return "'"
    if symbol == '+':
        return ''
    if symbol == '"':
        return '!'
    if symbol == '/':
        return '.'
    if symbol == '-':
        return ','


def dividing_into_lines(_list):
    temp_list = ['\n']
    two_dimensional_list = []
    for word in _list:
        temp_list.append(word)
        if ('.' in word or '!' in word) and _list.index(word) != 0:
            two_dimensional_list.append(temp_list)
            temp_list = ['\n']
    return two_dimensional_list


def shift_word(shift, word_str):
    word_list = list(word_str)
    for transfer_symbol in range(shift):
        word_list.insert(0, word_list[len(word_list) - 1])
        word_list.pop()
    word_str_shift = ''
    for symbol in word_list:
        word_str_shift += symbol
    return word_str_shift


def decoded_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = 51

    caesar_decoder_symbol_list = [alphabet[(alphabet.index(symbol) + shift) % len(alphabet)]
                      if symbol.isalpha()
                      else special_symbol(symbol)
                      for symbol in text]

    caesar_decoder_str = ''
    for symbol in caesar_decoder_symbol_list:
        caesar_decoder_str += symbol

    caesar_decoder_word_list = caesar_decoder_str.split(' ')
    text_by_lines_list = dividing_into_lines(caesar_decoder_word_list)
    caesar_decoder_word_shift_list = [shift_word(text_by_lines_list.index(line) + 3, word)
                                      for line in text_by_lines_list
                                      for word in line]

    decoded_text = ' '.join(caesar_decoder_word_shift_list)

    return decoded_text


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
       'uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
       'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ' \
       'ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ' \
       'ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq ' \
       'tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

decoded_text(text)

print(decoded_text(text))