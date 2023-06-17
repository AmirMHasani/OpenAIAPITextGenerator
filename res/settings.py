from tkinter import *
from PIL import Image, ImageTk
import json,os




def settings_(base_frame):
    settings_window = Toplevel(base_frame)
    settings_window.attributes('-topmost',1)

    load_settings_boolenaVar = BooleanVar()
    load_settings_boolenaVar.set(0)

    global looded_data
    looded_data = {
        "model": "text-davinci-003",
        "temperature": "0.7",
        "max_tokens": "2800",
        "top_p": "1.0",
        "best_of": "1",
        "frequency_penalty": "0.0",
        "presence_penalty": "0.0"
    }
    if os.path.exists('res/data.log'):
        load_settings_boolenaVar.set(1)
        f = open('res/data.log')
        looded_data = json.load(f)
        




    main_canvas = Canvas(settings_window,bg='white',width=800,height=600, border=0,borderwidth=0,highlightthickness=0)
    main_canvas.pack(anchor='w')

    mode_canvas = Frame(main_canvas,bg='white',width=200,height=600,border=0,borderwidth=0,highlightthickness=1,padx=10)
    mode_canvas.pack(anchor='w',side=LEFT,expand=True,fill=Y)


    model_canvas = Frame(main_canvas,bg='white',width=250,height=600,border=0,borderwidth=0,highlightthickness=1,padx=10)
    model_canvas.pack(anchor='nw',side=LEFT,expand=True,fill=Y)

    model__complete__canvas = Frame(model_canvas,bg='white',width=250,height=600,border=0,borderwidth=0,highlightthickness=0,padx=0)
    model__complete__canvas.pack(anchor='nw',side=LEFT)

    model__chat__canvas = Frame(model_canvas,bg='white',width=250,height=600,border=0,borderwidth=0,highlightthickness=0,padx=0)
    # model__chat__canvas.pack(anchor='w',side=LEFT)


    parameter_canvas = Frame(main_canvas,bg='white',width=350,height=600,border=0,borderwidth=0,highlightthickness=1,padx=10)
    parameter_canvas.pack(anchor='w',side=LEFT)






    selected_model_stringVar = StringVar()
    selected_model_stringVar.set('')

    previous_selected_model_stringVar = StringVar()
    previous_selected_model_stringVar.set('')



    model_stringVar = StringVar() 
    model_stringVar.set('')

    temperature_stringVar = StringVar()
    temperature_stringVar.set('')

    max_tokens_stringVar = StringVar()
    max_tokens_stringVar.set('')

    top_p_stringVar = StringVar()
    top_p_stringVar.set('')

    best_of_stringVar = StringVar()
    best_of_stringVar.set('')

    frequency_penalty_stringVar = StringVar()
    frequency_penalty_stringVar.set('')

    presence_penalty_stringVar = StringVar()
    presence_penalty_stringVar.set('')


    global selected_model_dict
    selected_model_dict = {}



    def selected_model_EL(e,model_type_name,scale_data):
        selected_model(model_type_name,scale_data)

    def selected_model(model_type_name,scale_data):
        global looded_data
        selected_model_stringVar.set(model_type_name)
        # print(previous_selected_model_stringVar.get(),selected_model_stringVar.get())
        if previous_selected_model_stringVar.get() != '':
            selected_model_dict[f'{str(previous_selected_model_stringVar.get())}_BTN']['fg'] = '#4e4f57'
        
        if previous_selected_model_stringVar.get() != selected_model_stringVar.get():
            selected_model_dict[f'{str(model_type_name)}_BTN']['fg'] = '#10a37f'
            # from_=0, to=100,length=300, resolution=0.01

            Temperature_scale['from_'] = scale_data['Temperature']['minimum']
            Temperature_scale['to'] = scale_data['Temperature']['maximum']
            Temperature_scale['resolution'] = scale_data['Temperature']['step']
            value = (scale_data['Temperature']['maximum'])
            if selected_model_stringVar.get() == looded_data["model"]:
                value = looded_data["temperature"]
            else: 
                value = scale_data['Temperature']['maximum']
            Temperature_scale.set(value)
            temperature_stringVar.set(str(value))

            Maximumlength_scale['from_'] = scale_data['Maximum length']['minimum']
            Maximumlength_scale['to'] = scale_data['Maximum length']['maximum']
            Maximumlength_scale['resolution'] = scale_data['Maximum length']['step']
            if selected_model_stringVar.get() == looded_data["model"]:
                value = looded_data["max_tokens"]
            else: 
                value = scale_data['Maximum length']['maximum']
            Maximumlength_scale.set(value)
            max_tokens_stringVar.set(str(value))


            TopP_scale['from_'] = scale_data['Top P']['minimum']
            TopP_scale['to'] = scale_data['Top P']['maximum']
            TopP_scale['resolution'] = scale_data['Top P']['step']
            if selected_model_stringVar.get() == looded_data["model"]:
                value = looded_data["top_p"]
            else: 
                value = scale_data['Top P']['maximum']
            TopP_scale.set(value)
            top_p_stringVar.set(str(value))


            Frequencypenalty_scale['from_'] = scale_data['Frequency penalty']['minimum']
            Frequencypenalty_scale['to'] = scale_data['Frequency penalty']['maximum']
            Frequencypenalty_scale['resolution'] = scale_data['Frequency penalty']['step']
            if selected_model_stringVar.get() == looded_data["model"]:
                value = looded_data["frequency_penalty"]
            else: 
                value = scale_data['Frequency penalty']['minimum']
            Frequencypenalty_scale.set(value)
            frequency_penalty_stringVar.set(str(value))


            Presencepenalty_scale['from_'] = scale_data['Presence penalty']['minimum']
            Presencepenalty_scale['to'] = scale_data['Presence penalty']['maximum']
            Presencepenalty_scale['resolution'] = scale_data['Presence penalty']['step']
            if selected_model_stringVar.get() == looded_data["model"]:
                value = looded_data["presence_penalty"]
            else: 
                value = scale_data['Presence penalty']['minimum']
            Presencepenalty_scale.set(value)
            presence_penalty_stringVar.set(str(value))

            if 'Best of' in scale_data:
                Bestof_scale['state'] = NORMAL
                Bestof_scale_label['state'] = NORMAL
                
                Bestof_scale['from_'] = scale_data['Best of']['minimum']
                Bestof_scale['to'] = scale_data['Best of']['maximum']
                Bestof_scale['resolution'] = scale_data['Best of']['step']
                if selected_model_stringVar.get() == looded_data["model"]:
                    value = looded_data["best_of"]
                else: 
                    value = scale_data['Best of']['minimum']
                Bestof_scale.set(value)
                best_of_stringVar.set(str(value))
            else:
                Bestof_scale.set(0)
                best_of_stringVar.set(str(0))
                Bestof_scale['state'] = DISABLED
                Bestof_scale_label['state'] = DISABLED


            print_data()


        previous_selected_model_stringVar.set(model_type_name)



    def updateData(e):
        temperature_stringVar.set(str(Temperature_scale.get()))

        max_tokens_stringVar.set(str(Maximumlength_scale.get()))

        top_p_stringVar.set(str(TopP_scale.get()))

        best_of_stringVar.set(str(Bestof_scale.get()))

        frequency_penalty_stringVar.set(str(Frequencypenalty_scale.get()))

        presence_penalty_stringVar.set(str(Presencepenalty_scale.get()))

        print_data()

    def print_data():
        text = {
        "model" : str(selected_model_stringVar.get()),
        "temperature" : str(temperature_stringVar.get()),
        "max_tokens" : str(max_tokens_stringVar.get()),
        "top_p" : str(top_p_stringVar.get()),
        "best_of" : str(best_of_stringVar.get()),
        "frequency_penalty" : str(frequency_penalty_stringVar.get()),
        "presence_penalty" : str(presence_penalty_stringVar.get())
        }
        with open('res/data.log','w') as RF:
            RF.write(str(json.dumps(text,indent=4)))
        RF.close()

    

    info = 'Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.'
    Label(parameter_canvas,text='Temperature',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Temperature_scale = Scale(parameter_canvas,bg='white',font=('Arial','10','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    Temperature_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')

    info = 'The maximum number of tokens to generate. Requests can use up to 2,048 or 4,000 tokens shared between prompt and completion. The exact limit varies by model. (One token is roughly 4 characters for normal English text)'
    Label(parameter_canvas,text='Maximum length',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Maximumlength_scale = Scale(parameter_canvas,bg='white',font=('Arial','8','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    Maximumlength_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')

    info = 'Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.'
    Label(parameter_canvas,text='Top P',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    TopP_scale = Scale(parameter_canvas,bg='white',font=('Arial','8','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    TopP_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')

    info = 'How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model\'s likelihood to repeat the same line verbatim.'
    Label(parameter_canvas,text='Frequency penalty',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Frequencypenalty_scale = Scale(parameter_canvas,bg='white',font=('Arial','8','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    Frequencypenalty_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')

    info = 'How much to penalize new tokens based on whether they appear in the text so far. Increases the model\'s likelihood to talk about new topics.'
    Label(parameter_canvas,text='Presence penalty',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Presencepenalty_scale = Scale(parameter_canvas,bg='white',font=('Arial','8','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    Presencepenalty_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')

    info = "Generates multiple completions' server-side, and displays only the best. Streaming only works when set to 1. Since it acts as a multiplier on the number of completions, these parameters can eat into your token quota very quickly – use caution!"
    Bestof_scale_label = Label(parameter_canvas,text='Best of',bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0)
    Bestof_scale_label.pack(anchor='w')
    Label(parameter_canvas,text=info,bg='white',fg='#746C7D',justify=LEFT, wraplength=300,font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0).pack(anchor='w')
    Bestof_scale = Scale(parameter_canvas,bg='white',font=('Arial','8','normal'),from_=0, to=100,length=300, resolution=0.01,orient=HORIZONTAL,border=0,borderwidth=0,highlightthickness=0,command = updateData)
    Bestof_scale.pack(anchor='w')
    Label(parameter_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=0).pack(anchor='w')









    GPT_modeL = \
    {"Chat":
        {"gpt-4": 
            {"size" : 1, 
            "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
            "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
            "Top P" : {"minimum":0, "maximum":1,"step":0.01},
            "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
            "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
            },
        "gpt-3.5-turbo": 
            {"size" : 2, 
            "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
            "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
            "Top P" : {"minimum":0, "maximum":1,"step":0.01},
            "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
            "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
            },
        "gpt-3.5-turbo-0301": 
            {"size" : 2, 
            "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
            "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
            "Top P" : {"minimum":0, "maximum":1,"step":0.01},
            "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
            "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
            },
        },
        
    "Complete":
        {"GPT-3" :
            {"text-davinci-003" :
                {"size" : 1, 
                "tag" : "",
                "description": "Most capable model in the GPT-3 series. Can perform any task the other GPT-3 models can, often with higher quality, longer output and better instruction-following. It can process up to 4,000 tokens per request.",
                "strength" : "Complex intent, cause and effect, creative generation, search, summarization for audience",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":4000,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "text-curie-001" :
                {"size" : 2, 
                "tag" : "Formerly curie-instruct-beta-v2",
                "description": "Very capable, but faster and lower cost than text-davinci-003.",
                "strength" : "Language translation, complex classification, sentiment, summarization",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "text-babbage-001":
                {"size" : 3, 
                "tag" : "Formerly babbage-instruct-beta",
                "description": "Capable of straightforward tasks, very fast, and lower cost.",
                "strength" : "Moderate classification, semantic search",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "text-ada-001" :
                {"size" : 4, 
                "tag" : "Formerly ada-instruct-beta",
                "description": "Capable of simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.",
                "strength" : "Parsing text, simple classification, address correction, keywords",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "text-davinci-002":
                {"size" : 1, 
                "tag" : "",
                "description": "Second generation model in the GPT-3 series. Can perform any task the earlier GPT-3 models can, often with less context. It can process up to 4,000 tokens per request.",
                "strength" : "Complex intent, cause and effect, creative generation, search, summarization for audience",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":4000,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "text-davinci-001" :
                {"size" : 1, 
                "tag" : "Formerly davinci-instruct-beta-v3",
                "description": "Older version of the most capable model in the GPT-3 series. Can perform any task the other GPT-3 models can, often with less context.",
                "strength" : "Complex intent, cause and effect, creative generation, search, summarization for audience",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "davinci-instruct-beta" :
                {"size" : 1, 
                "tag" : "davinci-instruct-beta",
                "description": "This is an older model. We recommend using our latest GPT-3 models instead.",
                "strength" : "Shorter and more naturally phrased prompts, complex intent, cause and effect",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "davinci" :
                {
                "size" : 1, 
                "tag" : "",
                "description": "This model is part of our original, base GPT-3 series. We recommend using our latest GPT-3 models instead. Learn more.",
                "strength" : "Complex intent, cause and effect, creative generation, search, summarization for audience.",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },
            "curie-instruct-beta " :
                {
                "size" : 2, 
                "tag" : "",
                "description": "This is an older model. We recommend using our latest GPT-3 models instead.",
                "strength" : "Shorter and more naturally phrased prompts, language translation, complex classification, sentiment",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "curie":
                {
                "size" : 2, 
                "tag" : "This model is part of our original, base GPT-3 series. We recommend using our latest GPT-3 models instead. Learn more.",
                "description": "",
                "strength" : "Language translation, complex classification, sentiment,summarization",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "babbage" :
                {"size" : 3, 
                "tag" : "This model is part of our original, base GPT-3 series. We recommend using our latest GPT-3 models instead. Learn more.",
                "description": "",
                "strength" : "Moderate classification, semantic search",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "ada" :
                {
                "size" : 4 , 
                "tag" : "",
                "description": "This model is part of our original, base GPT-3 series. We recommend using our latest GPT-3 models instead. Learn more.",
                "strength" : "Parsing text, simple classification, address correction, keywords",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                }
            },



        "CODEX" :
            {"code-davinci-002" :
                {"size" : 1 , 
                "tag" : "",
                "description": "Most capable model in the Codex series, which can understand and generate code, including translating natural language to code. It can process up to 4,000 tokens per request.",
                "strength" : "Our JavaScript Sandbox demo application uses this model to translate instructions into JS.",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":8000,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                },

            "code-cushman-001" :
                {"size" : 1, 
                "tag" : "Formerly cushman-codex",
                "description": "Almost as capable as code- davinci-002, but slightly faster. Part of the Codex series, which can understand and generate code.Our JavaScript Sandbox demo application uses this model to translate instructions into JS.",
                "strength" : "Real-time applications where low latency is preferable",
                "Temperature" : {"minimum":0, "maximum":1,"step":0.01},
                "Maximum length" : {"minimum":1, "maximum":2048,"step":1},
                "Top P" : {"minimum":0, "maximum":1,"step":0.01},
                "Frequency penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Presence penalty" : {"minimum":0, "maximum":2,"step":0.01},
                "Best of" : {"minimum":1, "maximum":20,"step":1},
                }
            }
        }
        }
            



    
    imageTk = {
        'gpt_complete' : ImageTk.PhotoImage(Image.open('res/gpt_complete.png').resize((20,20),Image.LANCZOS)),
        'gpt_chat' : ImageTk.PhotoImage(Image.open('res/gpt_chat.png').resize((20,20),Image.LANCZOS)),
        '1' : ImageTk.PhotoImage(Image.open('res/circle.png').resize((14,14),Image.LANCZOS)),
        '2' : ImageTk.PhotoImage(Image.open('res/circle.png').resize((10,10),Image.LANCZOS)),
        '3' : ImageTk.PhotoImage(Image.open('res/circle.png').resize((6,6),Image.LANCZOS)),
        '4' : ImageTk.PhotoImage(Image.open('res/circle.png').resize((4,4),Image.LANCZOS)),
    }
        
    def show_chat():
        global mode_name_LBL
        mode_name_LBL['Chat']['fg'] = '#10a37f'
        mode_name_LBL['Complete']['fg'] = '#4e4f57'
        model__complete__canvas.pack_forget()
        model__chat__canvas.pack(anchor='n')
        

    def show_chat_EL(e):
        show_chat()
        
        
    def show_complete():
        global mode_name_LBL   
        mode_name_LBL['Chat']['fg'] = '#4e4f57'
        mode_name_LBL['Complete']['fg'] = '#10a37f'
        model__chat__canvas.pack_forget()
        model__complete__canvas.pack(anchor='n')
             
    def show_complete_EL(e):  
        show_complete()   
    



    global mode_name_LBL
    mode_name_LBL = {}
    def each_mode_fun(mode_name,mode_image,type='Complete'):
        global mode_name_LBL
        mode_frame = Frame(mode_canvas,bg='white',width=400,border=0,borderwidth=0,highlightthickness=0,pady=5)
        mode_frame.pack(anchor='w')
        mode_ILBL = Label(mode_frame,fg='#4e4f57',bg='white',border=0,borderwidth=0,highlightthickness=0,padx=10)
        mode_ILBL['image'] = mode_image
        mode_ILBL.image = mode_image
        mode_ILBL.pack(anchor='w',side=LEFT)

        adjustment_frame = Frame(mode_frame,border=0,borderwidth=0,highlightthickness=0,bg='red')
        adjustment_frame.pack(anchor='w',side=LEFT)

        if type == 'Complete' : fgcolor = '#10a37f'
        else: fgcolor = '#4e4f57'

        Label(adjustment_frame,fg=fgcolor,bg='white',width=15,font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=10).grid(row=1,column=1,sticky='w')
        mode_name_LBL[type] = Label(adjustment_frame,text=mode_name,fg=fgcolor,bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=10)
        mode_name_LBL[type].grid(row=1,column=1,sticky='w')
        # Label(mode_frame,bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=30).pack(anchor='w',side=LEFT)
        
        for each_widgets in mode_frame.winfo_children():
            if type == 'Chat': each_widgets.bind("<Button-1>",show_chat_EL)
            else:  each_widgets.bind("<Button-1>",show_complete_EL)

        for each_widgets in adjustment_frame.winfo_children():
            if type == 'Chat': each_widgets.bind("<Button-1>",show_chat_EL)
            else:  each_widgets.bind("<Button-1>",show_complete_EL)
        


    def each_model_type_fun(model_type_name,padx):
        mode_frame = Frame(model__complete__canvas,bg='white',border=0,borderwidth=0,highlightthickness=0,pady=10)
        mode_frame.pack(anchor='w')
        mode_name_LBL = Label(mode_frame,text=model_type_name,fg='#4e4f57',bg='white',font=('Arial','12','bold'),border=0,borderwidth=0,highlightthickness=0,padx=10)
        mode_name_LBL.pack(anchor='w',side=LEFT)
        Label(mode_frame,bg='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=padx).pack(anchor='w',side=LEFT)

    def each_model_fun(model_type_name,model_image,scale_data,type=''):
        global selected_model_dict
        if type!='Chat':            
            selected_model_dict[f'{str(model_type_name)}_mode_frame'] = Frame(model__complete__canvas,border=0,bg='white',borderwidth=0,highlightthickness=0,pady=5)
        else:
            selected_model_dict[f'{str(model_type_name)}_mode_frame'] = Frame(model__chat__canvas,border=0,bg='white',borderwidth=0,highlightthickness=0,pady=5)

        selected_model_dict[f'{str(model_type_name)}_mode_frame'].pack(anchor='w',expand=True,fill=X)
        selected_model_dict[f'{str(model_type_name)}_mode_frame'].bind('<Button-1>',lambda e,model_type_name=model_type_name,scale_data=scale_data: selected_model_EL(e,model_type_name,scale_data))

        selected_model_dict[f'{str(model_type_name)}_BTN'] = Button(selected_model_dict[f'{str(model_type_name)}_mode_frame'],text=model_type_name,fg='#4e4f57',bg='white',activeforeground='#746C7D',activebackground='white',font=('Arial','12','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0)
        selected_model_dict[f'{str(model_type_name)}_BTN'].pack(anchor='w',side=LEFT)
        selected_model_dict[f'{str(model_type_name)}_BTN'].bind('<Button-1>',lambda e,model_type_name=model_type_name,scale_data=scale_data: selected_model_EL(e,model_type_name,scale_data))

        selected_model_dict[f'{str(model_type_name)}_ILBL'] = Label(selected_model_dict[f'{str(model_type_name)}_mode_frame'],border=0,fg='#4e4f57',bg='white',borderwidth=0,highlightthickness=0,padx=10)
        selected_model_dict[f'{str(model_type_name)}_ILBL']['image'] = imageTk[model_image]
        selected_model_dict[f'{str(model_type_name)}_ILBL'].image = imageTk[model_image]
        selected_model_dict[f'{str(model_type_name)}_ILBL'].pack(anchor='e',side=RIGHT)
        selected_model_dict[f'{str(model_type_name)}_ILBL'].bind('<Button-1>',lambda e, model_type_name=model_type_name,scale_data=scale_data: selected_model_EL(e,model_type_name,scale_data))


        






        
    previous_selected_model = ""
    previous_selected_model_scale = ""
    previous_selected_model_type = ""
    for each_mode in GPT_modeL:
        if each_mode == 'Complete':
            each_mode_fun(each_mode,imageTk['gpt_complete'])
        
            for each_model_Type in GPT_modeL[each_mode]:
                if each_model_Type == 'GPT-3' : each_model_type_fun(each_model_Type,92-2)
                elif each_model_Type == 'CODEX' : each_model_type_fun(each_model_Type,86-2)
                Frame(model__complete__canvas,height=2,width=250,bg='#F5F5F7').pack()
                for each_model in GPT_modeL[each_mode][each_model_Type]:
                    model_size = GPT_modeL[each_mode][each_model_Type][each_model]['size']
                    scale_data = GPT_modeL[each_mode][each_model_Type][each_model]
                    each_model_fun(each_model,str(model_size),scale_data)
                    Frame(model__complete__canvas,height=1,width=250,bg='#F5F5F7').pack()
                    # Check Previous
                    if looded_data["model"] == each_model:
                        # selected_model(each_model,scale_data)
                        # show_complete()
                        previous_selected_model = each_model
                        previous_selected_model_scale = scale_data
                        previous_selected_model_type = "Complete"
        
        elif each_mode == 'Chat':
            each_mode_fun(each_mode,imageTk['gpt_chat'],type='Chat')
            for each_model_name in GPT_modeL[each_mode]:
                scale_data = GPT_modeL[each_mode][each_model_name]
                model_size = GPT_modeL[each_mode][each_model_name]['size']
                each_model_fun(each_model_name,str(model_size),scale_data,type='Chat')
                Frame(model__chat__canvas,height=1,width=250,bg='#F5F5F7').pack()

                if looded_data["model"] == each_model_name:
                        # selected_model(each_model_name,scale_data)
                        # show_chat()
                        previous_selected_model = each_model_name
                        previous_selected_model_scale = scale_data
                        previous_selected_model_type = "Chat"

        
    if previous_selected_model != "":
        selected_model(previous_selected_model,previous_selected_model_scale)
        if previous_selected_model_type == "Chat":
            show_chat()
        else:
            show_complete()





    # configure_fun()       
            

    # Label(model_canvas,bg='white',font=('Arial','8','normal'),border=0,borderwidth=0,highlightthickness=0,padx=0,pady=20+34).pack(anchor='w')

    def center_window(window,width=0,height=0):
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))


    app_icon = Image.open("res/settings.png")
    app_icon = ImageTk.PhotoImage(app_icon.resize((16,16),Image.LANCZOS))
    settings_window.iconphoto(False, app_icon)
    settings_window.title('GPT Tuning ')
    settings_window.resizable(0,0)
    center_window(settings_window,width=790,height=700)
    settings_window.transient(base_frame)
    # settings_window.geometry('790x700')
    # settings_window.mainloop()


# root = Tk()
# settings_(root)
# root.mainloop()