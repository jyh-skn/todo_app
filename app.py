import streamlit as st

# CSS 적용
st.markdown(
    """
    <style>
    .st-emotion-cache-1frkdi4 
    p {
        margin-top: 7px;
    }
    del {
        color: #DCDCDC;
    } 
    </style>
    """,
    unsafe_allow_html=True
)

st.title('☑️TO-DO☑️')

class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 리스트 안에 있을 때, 리스트 안의 요소들을 출력하면, __repr__을 써야 출력됨.
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

        # repr은 eval()로 다시 객체로 바쑬 수 있는 문자열 형태로
        # return f'Todo(task={self.__task}, done={self.__done})'

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

# __repr__ 심화 설명 -> 이해X
# todo = Todo('assignment')
# print(todo)
# print(Todo(task='dinner', done=False))
# #
# todo2 = eval(repr(todo))
# print(todo2)

# Todo 객체를 list에 쌓음 -> 추가할 할일을 작성하면 실행.
def add_todo():
    print(f'함수가 호출 될 때 주머니에 담긴 값: {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    # print(todo)
    st.session_state.todos.append(todo)
    st.session_state.new_task = ""

def togle_done(index:int):
    todo = st.session_state.todos[index]
    todo.set_done(not todo.get_done())

# todos(todo객체를 담을 리스트 초기화)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다.(session_state에 새로운 키 초기화)
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo)  # input 창에 내용을 작성(기존과 다른 내용)하고
                                                                         # 엔터하면 add_todo함수 호출

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # checked = st.checkbox(
        #     label=f"{i + 1} 번째 todo: {todo}",
        #     key=f"todo_{i}"
        # )

        # st.write(f'{i}번째 todo => {todo}')
        col1, col2 = st.columns([0.1, 0.9]) # 비율은 취향껏
        col1.checkbox(f'{i + 1}', value=todo.get_done(), key=f'done_{i}', on_change=togle_done, args=(i, ))
        col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())

        # st.divider()
else:
    st.write('할일 추가')

# pip list하면 현재 가상환경(pystudy_env)에 있는 도구들(패키지들)을 알 수 있음.
# streamlit에 배포하기 위해 github에 올릴 때, requirements.txt로 만들어, push해줘야 함.
# pip list --format=freeze > requirements.txt
# 만약 충돌이 나는 경우,
#   1) requirements.txt 중에서 win 검색 -> window 환경에서만 적용 -> streamlit 배포 환경은 linux이기 때문에 충돌
#       1. pywin32==311
#       2. pywinpty=2.0.15
#       3. win_inet_pton==1.1.0
#   2) LLM을 활용해서 해당 라이브러리에서 적합한 버전으로 수정&삭제하면 배포가능
