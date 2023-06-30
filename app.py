# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


#라이브러리
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

#앱 정의
app = Dash(__name__)
server = app.server


#데이터
df1 = pd.read_csv('test.csv')
df1['YEAR']=df1.PRD_DE.astype(str).str[:4]
df1['MONTH']=df1.PRD_DE.astype(str).str[4:].astype(int)

df2 = pd.read_csv('test1.csv')
df2['YEAR']=df2.PRD_DE.astype(str).str[:4]
df2['MONTH']=df2.PRD_DE.astype(str).str[4:].astype(int)

df3 = pd.read_csv('test2.csv')
df3['YEAR']=df3.PRD_DE.astype(str).str[:4]
df3['MONTH']=df3.PRD_DE.astype(str).str[4:].astype(int)

df4 = pd.read_csv('test3.csv')
df4['YEAR']=df4.PRD_DE.astype(str).str[:4]
df4['MONTH']=df4.PRD_DE.astype(str).str[4:].astype(int)

df=pd.concat([df1,df2,df3,df4])

#유가증권 산업코드 일치
df=df.replace('13102792752A.01','13102792751A.01')
df=df.replace('13102792752A.02','13102792751A.02')
df=df.replace('13102792752A.03','13102792751A.03')
df=df.replace('13102792752A.04','13102792751A.04')
df=df.replace('13102792752A.05','13102792751A.05')
df=df.replace('13102792752A.06','13102792751A.06')
df=df.replace('13102792752A.07','13102792751A.07')
df=df.replace('13102792752A.08','13102792751A.08')
df=df.replace('13102792752A.09','13102792751A.09')
df=df.replace('13102792752A.10','13102792751A.10')
df=df.replace('13102792752A.11','13102792751A.11')
df=df.replace('13102792752A.12','13102792751A.12')
df=df.replace('13102792752A.13','13102792751A.13')
df=df.replace('13102792752A.14','13102792751A.14')
df=df.replace('13102792752A.15','13102792751A.15')
df=df.replace('13102792752A.16','13102792751A.16')
df=df.replace('13102792752A.17','13102792751A.17')
df=df.replace('13102792752A.18','13102792751A.18')
df=df.replace('13102792752A.19','13102792751A.19')
df=df.replace('13102792752A.20','13102792751A.20')
df=df.replace('13102792752A.21','13102792751A.21')

#코스닥 산업코드 일치
df=df.replace('13102792766A.01','13102792767A.01')
df=df.replace('13102792766A.31','13102792767A.31')
df=df.replace('13102792766A.32','13102792767A.32')
df=df.replace('13102792766A.02','13102792767A.02')
df=df.replace('13102792766A.03','13102792767A.03')
df=df.replace('13102792766A.04','13102792767A.04')
df=df.replace('13102792766A.05','13102792767A.05')
df=df.replace('13102792766A.06','13102792767A.06')
df=df.replace('13102792766A.07','13102792767A.07')
df=df.replace('13102792766A.08','13102792767A.08')
df=df.replace('13102792766A.09','13102792767A.09')
df=df.replace('13102792766A.10','13102792767A.10')
df=df.replace('13102792766A.11','13102792767A.11')
df=df.replace('13102792766A.12','13102792767A.12')
df=df.replace('13102792766A.13','13102792767A.13')
df=df.replace('13102792766A.14','13102792767A.14')
df=df.replace('13102792766A.33','13102792767A.33')
df=df.replace('13102792766A.15','13102792767A.15')
df=df.replace('13102792766A.16','13102792767A.16')
df=df.replace('13102792766A.34','13102792767A.34')
df=df.replace('13102792766A.17','13102792767A.17')
df=df.replace('13102792766A.18','13102792767A.18')
df=df.replace('13102792766A.19','13102792767A.19')
df=df.replace('13102792766A.20','13102792767A.20')
df=df.replace('13102792766A.21','13102792767A.21')
df=df.replace('13102792766A.22','13102792767A.22')
df=df.replace('13102792766A.23','13102792767A.23')
df=df.replace('13102792766A.24','13102792767A.24')
df=df.replace('13102792766A.25','13102792767A.25')
df=df.replace('13102792766A.26','13102792767A.26')
df=df.replace('13102792766A.27','13102792767A.27')
df=df.replace('13102792766A.28','13102792767A.28')
df=df.replace('13102792766A.29','13102792767A.29')
df=df.replace('13102792766A.30','13102792767A.30')

#수익 일치
df=df.replace('13102792767B.02','13102792751B.02')
df=df.replace('13102792767B.03','13102792751B.03')
df=df.replace('13102792767B.05','13102792751B.05')
df=df.replace('13102792767B.07','13102792751B.07')
df=df.replace('13102792767B.10','13102792751B.10')

#비율 일치
df=df.replace('13102792766B.07','13102792752B.07')
df=df.replace('13102792766B.08','13102792752B.08')
df=df.replace('13102792766B.09','13102792752B.09')
df=df.replace('13102792766B.10','13102792752B.10')
df=df.replace('13102792766B.11','13102792752B.11')
df=df.replace('13102792766B.12','13102792752B.12')

#변경
df=df.replace('매출액','매출액(백만원)')
df=df.replace('영업이익','영업이익(백만원)')
df=df.replace('당기순이익','당기순이익(백만원)')
df=df.replace('자기자본이익률','자기자본이익률(%)')
df=df.replace('매출액이익률','매출액이익률(%)')
df=df.replace('자기자본비율','자기자본비율(%)')
df=df.replace('부채비율','부채비율(%)')
df=df.replace('유보율','유보율(%)')
df=df.replace('유동비율','유동비율(%)')
df=df.replace('고정비율','고정비율(%)')
df=df.replace('차입금의존도','차입금의존도(%)')


#드롭다운 입력값 리스트 만들기
industry_list = list(zip(df.C1_NM.unique(), df.C1.unique()))
profit_list = list(zip(df.C2_NM.unique(), df.C2.unique()))
year_list = list(zip(df.YEAR.unique(), df.YEAR.unique()))
year_list.reverse()

#초기값설정
industry_value='13102792751A.01'
profit_value='13102792751B.02'
year_value=['2023','2022']


#그래프
fig = go.Figure()

for year in year_value:
    #드롭다운 입력값에 맞는 데이터만 추출
    df_graph = df[(df.C1==industry_value) & (df.C2==profit_value) & (df.YEAR==year)]
    fig.add_trace(go.Scatter(x=df_graph.MONTH,y=df_graph.DT,name=year))
    fig.update_xaxes(range=[0.5,12.5],
                     ticktext=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
                     tickvals=[1,2,3,4,5,6,7,8,9,10,11,12])

#웹페이지 생성
app.layout = html.Div([
    html.H3('Analytical Procedures(산업별,유가증권,코스닥)',style={'textAlign':'center'}),
    html.H3('매년 4월 통계가 전년도 사업보고서를 합산한 수치이며, 따라서 연 통계는 다음해 4월 기준의 수치가 해당합니다.',style={'textAlign':'center'}),
    html.H3('모든 데이터는 통계청 KOSIS OPEN API로부터 제공되었습니다',style={'textAlign':'center'}),
    html.H3('(ekenis@naver.com)',style={'textAlign':'center'}),
    html.Div([
        dcc.Dropdown(id='industry_dropdown',
            options=[{'label':i,'value':j} for i,j in industry_list],
            value = industry_value,
            searchable=False,
            style=dict(width='100%')
        ),
        dcc.Dropdown(id='profit_dropdown',
            options=[{'label':i,'value':j} for i,j in profit_list],
            value = profit_value,
            searchable=False,
            style=dict(width='100%')
        ),
        dcc.Dropdown(id='year_dropdown',
            options=[{'label':i,'value':j} for i,j in year_list],
            value = year_value,
            searchable=False,
            multi=True,
            style=dict(width='100%')
        )
    ]),
    html.Div([
        dcc.Graph(id='graph',figure=fig)
        ]
    )
])

@app.callback(
    Output('graph','figure'),
    Input('industry_dropdown','value'),
    Input('profit_dropdown','value'),
    [Input('year_dropdown','value')]
)
def update_graph(industry_val,profit_val,year_val):
    fig = go.Figure()
    for year in year_val:
        #드롭다운 입력값에 맞는 데이터만 추출
        df_graph = df[(df.C1==industry_val) & (df.C2==profit_val) & (df.YEAR==year)]
        fig.add_trace(go.Scatter(x=df_graph.MONTH,y=df_graph.DT,name=year))
        fig.update_xaxes(range=[0.5,12.5],
                     ticktext=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
                     tickvals=[1,2,3,4,5,6,7,8,9,10,11,12])
    return fig




#실행명령
if __name__ == '__main__':
    app.run(debug=True)
