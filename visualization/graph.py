import matplotlib.pyplot as plt


def hangle(): # 한글 깨짐 처리
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


def create_graph(df):
    plt.scatter(df[0], df[1])
    plt.xlabel('tag_count')
    plt.ylabel('letter_count')
    plt.show()


def bar_graph(df, name):
    hangle()
    plt.title("기분 별 " + name)
    plt.bar(['#happy', '#sad'], df,
            width=0.5,
            color='grey')
    plt.ylabel(name)
    plt.show()


def bar_graph_v2(df):
    # plt.barh(['#happy', '#sad'])
    plt.barh(df, 'BaseValue', 25)
