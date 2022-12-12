# 必要なライブラリをインポートする
import streamlit as st
import streamlit.components.v1 as stc

import time

from ..generic import func_html


# @st.cache(allow_output_mutation=True)
def view_lesson():

    # ポータルフラグを確認
    if st.session_state['portal_flg'] == True:
        return


    if st.sidebar.button('test'):
        pass

    # タイトル
    # st.header('アクティビティ「Pythonを使ってみよう」')

    step_name = st.sidebar.radio("手順を選択してください",("手順1", "手順2", "手順3", "手順4", "手順5", "手順6"), horizontal=True)
    flg_answer = st.sidebar.checkbox("お手本を確認する")

    # # セッションステートを初期化する
    # if 'step1_flg' not in st.session_state:
    #     st.session_state.step1_flg = False

    # if st.sidebar.button('プログラムを開く'):
    #     st.session_state.step1_flg = step_name
    #     print(st.session_state.step1_flg)

    ##### 手順1 #####
    if step_name == '手順1':

        ### サイドバーエリア ###
        # st.sidebar.markdown('説明')
        st.sidebar.success('プログラムを書いてコンピュータに指示を与えましょう。指示を与えるにはプログラミングで「命令」をします。\n\n［プログラミングエリア］に書かれているのが Python の命令です。')
        ret_exec_button = st.sidebar.button('プログラムの実行')
        # st.session_state.step1_flg = ret_exec_button

        # ret_init_button = st.sidebar.button('プログラムを戻す')
        # if ret_init_button == True:
        #     text_value = 'print(1+2+3)'

        ### メインエリア ###
        # if st.session_state.step1_flg == False:

        # プログラミングエリア
        text_value = 'print(100)'
        txt_input = st.text_area('プログラミングエリア', value=text_value ,max_chars=500, height=1)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = 'print(100)'
            st.code(text_value)


        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = '<font color=blue>print</font> は値を出力する命令です<br>では <font color=blue>print(100)</font> という命令を実行すると どうなると思いますか？<br>結果を予想してから「プログラムの実行」ボタンを押しましょう'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret)

        else:

            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:

                exec(txt_output)    # 実行

                # 吹き出し（女子）
                file_name = 'ai030.png'
                str_message = '実行結果エリアに <font color=green>100</font> と出力されました'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

                # 枠（説明）
                ret = func_html.make_html_frame("解説", "<font color=blue>print</font> はカッコ<font color=blue>()</font>で囲まれた値を実行結果に出力します。Pythonでもっともよく使われる命令の1つです。<br>実行結果エリアに注目してください。カッコの中にある <font color=green>100</font> が実行結果として出力されました。<br>")
                stc.html(ret,height=175)
                st.caption('メニューから次の手順を選択しましょう')

            except:
                print('Error')
                st.error('エラー！')

                # 吹き出し（先生）
                file_name = 'ai010.png'
                str_message = 'エラー（プログラムの誤り）が発生したようです<br>プログラミングエリアの内容に誤りがないか確認してください<br>誤りを修正したら もう一度「プログラムの実行」ボタンを押しましょう'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=200)
                st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')

    ##### 手順2 #####
    if step_name == '手順2':

        ### サイドバーエリア ###
        ret_exec_button = st.sidebar.button('プログラムの実行')

        ### メインエリア ###

        # プログラミングエリア
        text_value = 'print(300-200+50)'
        txt_input = st.text_area('プログラミングエリア', value=text_value ,max_chars=500, height=1)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = 'print(300-200+50)'
            st.success(text_value)

        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = '先ほどと同じ <font color=blue>print</font> 命令ですが <font color=blue>()</font>で囲まれているのが数式です<br>実行すると どうなると思いますか？<br>結果を予想してから「プログラムの実行」ボタンを押しましょう'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret,height=200)

        else:
            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:
                exec(txt_output)    # 実行

                # 吹き出し（男子）
                file_name = 'ai020.png'
                str_message = '今度は  <font color=green>150</font> と出力されたな<br><font color=green>300-200+50</font> を計算すると 150 だからかな？'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

                # 枠（説明）
                ret = func_html.make_html_frame("解説", "<font color=blue>print</font> は カッコ<font color=blue>()</font>で囲まれた値が<font color=red>数式</font>の場合は、答えを計算して出力します。<br>実行結果エリアに注目してください。<br>カッコの中身である<font color=green>300-200+50</font>が計算されて <font color=green>150</font> という実行結果が出力されました。")
                stc.html(ret,height=150)
                st.caption('メニューから次の手順を選択しましょう')

            except:
                print('Error')
                st.error('エラー！')

                # 吹き出し（先生）
                file_name = 'ai010.png'
                str_message = 'エラー（プログラムの誤り）が発生したようです<br>プログラミングエリアの内容に誤りがないか確認してください<br>誤りを修正したら もう一度「プログラムの実行」ボタンを押しましょう'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=200)
                st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')


    ##### 手順3 #####
    if step_name == '手順3':

        ### サイドバーエリア ###
        ret_exec_button = st.sidebar.button('プログラムの実行')

        ### メインエリア ###

        # プログラミングエリア
        text_value = 'print(2×3×4)'
        txt_input = st.text_area('プログラミングエリア', value=text_value ,max_chars=500, height=1)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = 'print(2×3×4)'
            st.code(text_value)

        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = '今度は <font color=blue>print</font>命令の <font color=blue>()</font> で囲まれているのが <font color=red>かけ算</font>の数式です<br>実行すると <font color=green>2×3×4</font> の計算結果は出力されるでしょうか？<br>結果を予想してから「プログラムの実行」ボタンを押しましょう'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret,height=200)

        else:
            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:
                exec(txt_output)    # 実行

                # 吹き出し（先生）
                file_name = 'ai010.png'
                str_message = 'この手順ではプログラムの「エラー（誤り）」を体験します<br>お手本をコピーして もう一度 実行してください'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

            except Exception as e:
                print('Error')
                st.error('エラーが発生しました！')
                # st.error(e)

                # 吹き出し（女子）
                file_name = 'ai030.png'
                str_message = 'プログラムが正しく動きませんでした<br>どこかが間違っていたのでしょうか…？'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=150)
                
                # 枠（説明）
                ret = func_html.make_html_frame("解説", "プログラムの誤りを<font color=red>「エラー」</font>といいます。プログラムを正しく動かすには、エラーを修正する必要があります。<br>この後の手順でエラーを修正しましょう。")
                stc.html(ret,height=175)
                st.caption('メニューから次の手順を選択しましょう')

                # st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')


    ##### 手順4 #####
    if step_name == '手順4':

        ### サイドバーエリア ###
        ret_exec_button = st.sidebar.button('プログラムの実行')

        ### メインエリア ###

        # プログラミングエリア
        text_value = 'print(2*3*4)'
        txt_input = st.text_area('プログラミングエリア', value=text_value ,max_chars=500, height=1)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = 'print(2*3*4)'
            st.code(text_value)

        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = 'プログラミングでは <font color=red>かけ算</font>の記号は <font color=blue>×</font> ではなく <font color=blue>*</font>（アスタリスク）を使用します<br>さきほどのプログラムの <font color=blue>×</font> をすべて <font color=blue>*</font> に修正しました。実行して動作を確認しましょう'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret,height=200)

        else:
            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:
                exec(txt_output)    # 実行

                # 吹き出し（先生）
                file_name = 'ai020.png'
                str_message = '今度は正しく計算できたよ<br>俺たちが普段 使っている演算記号と違うから 注意が必要だな'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

                # 枠（説明）
                ret = func_html.make_html_frame("解説", "Pythonでは、<font color=red>かけ算</font>の記号は <font color=blue>*</font>（アスタリスク）を使用します。また、<font color=red>割り算</font>の記号は「÷」ではなく、<font color=blue>/</font>（スラッシュ）を使用します。<br>数学で使う記号と異なりますので気を付けましょう。")
                stc.html(ret,height=150)
                st.caption('メニューから次の手順を選択しましょう')

            except Exception as e:
                print('Error')
                st.error('エラーが発生しました！')
                # st.error(e)

                # 吹き出し（女子）
                file_name = 'ai030.png'
                str_message = 'プログラムが正しく動きませんでした<br>どこかが間違っていたのでしょうか…？'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=150)

                # st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')

    ##### 手順5 #####
    if step_name == '手順5':

        ### サイドバーエリア ###
        ret_exec_button = st.sidebar.button('プログラムの実行')

        ### メインエリア ###

        # プログラミングエリア
        text_value = """a = 10
b = 20
print(a+b)
        """
        txt_input = st.text_area('プログラミングエリア', value=text_value ,max_chars=500, height=1)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = """a = 10
b = 20
print(a+b)
            """
            st.code(text_value)

        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = '今度はプログラムが3行に増えました<br>1行目と2行目では <font color=blue>=</font>（イコール）を使っていますね<br>さて、どんな結果になると思いますか？'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret,height=200)

        else:
            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:
                exec(txt_output)    # 実行

                # 吹き出し（先生）
                file_name = 'ai030.png'
                str_message = '実行結果には<font color=green> 30 </font>と出力されました<br><font color=blue> 10 </font>と<font color=blue> 20 </font>を足して 30 になったのかな？'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

                # 枠（説明）
                ret = func_html.make_html_frame("解説", "<font color=blue>a = 10</font> や <font color=blue>b = 20</font> の a や b は、「<font color=red>変数</font>」といいます。変数は高度なプログラムを作るのに必須の機能です。<br>詳しくは後日のレッスンで取り上げますので、どうぞお楽しみに。")
                stc.html(ret,height=150)
                st.caption('メニューから次の手順を選択しましょう')

            except Exception as e:
                print('Error')
                st.error('エラーが発生しました！')
                # st.error(e)

                # 吹き出し（先生）
                file_name = 'ai030.png'
                str_message = 'プログラムが正しく動きませんでした<br>どこかが間違っていたのでしょうか…？'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=150)

                # st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')


    ##### 手順6 #####
    if step_name == '手順6':

        ### サイドバーエリア ###
        ret_exec_button = st.sidebar.button('プログラムの実行')

        ### メインエリア ###

        # プログラミングエリア
        text_value = ''
        txt_input = st.text_area('プログラミングエリア', value=text_value, placeholder='ここにプログラムを記述しましょう' ,max_chars=500, height=300)

        if flg_answer == True:
            # プログラミングエリア
            st.markdown('プログラムのお手本')
            text_value = """a = 100
b = a + 100
if b > 100:
    print(' b は 100 より大きいです')
else:
    print(' b は 100 以下です')

            """
            st.code(text_value)

        # 実行ボタン
        if ret_exec_button == False:

            st.markdown('実行結果エリア')
            st.info('まだ実行されていません')

            # 吹き出し（先生）
            file_name = 'ai010.png'
            str_message = 'ここまでのプログラムを参考にして プログラミングエリアに好きなプログラムを書いて 実行してみましょう<br>参考として「お手本」に 少し長いプログラムを書いておきました'
            ret = func_html.make_html_balloon(file_name, str_message)
            stc.html(ret,height=200)

        else:
            with st.spinner('処理中です...'):
                time.sleep(3)

            st.markdown('実行結果エリア')

            #文字列の中身をプログラムとして実行
            txt_output = txt_input.replace('print', 'st.info')  # print文をst.infoに置換

            try:
                exec(txt_output)    # 実行

                # 吹き出し（女子）
                file_name = 'ai030.png'
                str_message = 'イメージした通りにプログラムは動きましたか？<br>いろいろとプログラムを書き換えて 実行してみてくださいね'
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret, height=150)

                # 枠（説明）
                ret = func_html.make_html_frame("Info", "お疲れ様でした。このアクティビティはここで終了です。引き続きタブレット（または、スマートフォン）でレッスンを進めましょう。")
                stc.html(ret,height=200)
                # st.caption('左のメニューから、次の手順を選択しましょう')

                # st.sidebar.success('このアクティビティはここまでです。引き続きタブレット（または、スマートフォン）でレッスンを進めましょう。')

            except:
                print('Error')
                st.error('エラー！')

                # 吹き出し（先生）
                file_name = 'ai010.png'
                str_message = 'エラー（プログラムの誤り）が発生したようです<br>プログラミングエリアの内容に誤りがないか確認してください<br>誤りを修正したら もう一度「プログラムの実行」ボタンを押しましょう'
                
                ret = func_html.make_html_balloon(file_name, str_message)
                stc.html(ret,height=200)
                st.caption('どうしても誤りが見つからない場合は お手本をコピーして もう一度 実行してみましょう')
