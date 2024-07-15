import gradio

import gradio as gr
from graphrag.query.cli import run_global_search, run_local_search


# 输入文本处理程序
def greet(query):
    return run_global_search(
        None,
        './ragtest',
        0,
        'Multiple Paragraphs',
        '"What is machinelearning?"',
    )


# 接口创建函数
# fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
# fn,inputs,outputs都是必填函数
demo = gr.Interface(fn=greet, inputs="text", outputs="text")


# python -m graphrag.query --root ./ragtest --method global "What is machinelearning?"
demo.launch(share=True)
