import tkinter as tk
from tkinter import messagebox
import os
import re


class DASS21App:
    def __init__(self, root):
        """Inicializa a aplicação e configura a janela principal."""
        self.root = root
        self.root.title("Sistema DASS-21")

        # Perguntas do questionário
        self.perguntas = [
            "01. Achei difícil me acalmar",
            "02. Senti minha boca seca",
            "03. Não consegui vivenciar nenhum sentimento positivo",
            "04. Senti falta de ar em alguns momentos, mesmo sem ter feito nenhum esforço físico",
            "05. Achei difícil ter iniciativa para fazer as coisas",
            "06. Tive a tendência de reagir de forma exagerada às situações",
            "07. Senti tremores (ex. nas mãos)",
            "08. Senti que estava sempre nervoso (a)",
            "09. Preocupei-me com situações em que eu pudesse entrar em pânico e parecesse ridículo (a)",
            "10. Senti que não tinha nada a esperar do futuro",
            "11. Senti-me agitado (a)",
            "12. Achei difícil relaxar",
            "13. Senti-me depressivo (a) e sem ânimo",
            "14. Fui intolerante com as coisas que me impediam de continuar o que eu estava fazendo",
            "15. Senti que ia entrar em pânico",
            "16. Não consegui me entusiasmar com nada",
            "17. Senti que não tinha valor como pessoa",
            "18. Senti que estava um pouco emotivo(a)/sensível demais",
            "19. Sabia que meu coração estava alterado mesmo não tendo feito nenhum esforço físico (ex. aumento da frequência cardíaca, disritmia cardíaca)",
            "20. Senti medo sem motivo",
            "21. Senti que a vida não tinha sentido"
        ]

        # Recomendações baseadas nos níveis de ansiedade, depressão e estresse
        self.recomendacoes = {
            'Normal': "Está tudo normal. Manter hábitos saudáveis, como alimentação equilibrada, sono regular e prática de "
                      "atividades físicas. Além disso, cultive hobbies e atividades prazerosas.",
            'Suave': "Sem preocupações por enquanto, considere a prática de técnicas de relaxamento, como meditação ou yoga. "
                     "Ademais, organize sua rotina e estabeleça prioridades para evitar a sensação de sobrecarga.",
            'Moderado': "Requer atenção. Vale a pena entender se foi algo pontual na última semana ou se é algo mais grave. "
                        "Você pode procurar grupos de apoio online ou em sua comunidade para te ajudar a lidar com essa situação ou "
                        "busque um psicólogo para um diagnóstico mais preciso.",
            'Severo': "Importante ficar atento. Procure um psicólogo para iniciar um tratamento adequado. Mesmo em momentos difíceis, "
                      "continue se cuidando. Alimente-se bem, durma o suficiente e evite o isolamento social.",
            'Extremamente Severo': "Procure ajuda profissional imediatamente. Entre em contato com um psicólogo, psiquiatra ou serviço "
                                   "de emergência."
        }

        # Inicializa variáveis
        self.respostas = []
        self.pergunta_atual = 0

        # Desafios diários
        self.desafios = {
            "Monday": "Medite por 5 minutos.",
            "Tuesday": "Pratique gratidão, agradecendo por mais um dia de vida.",
            "Wednesday": "Realize uma caminhada ao ar livre.",
            "Thursday": "Escreva sobre seus sentimentos em um diário.",
            "Friday": "Tire um tempo para um hobby que você ama.",
            "Saturday": "Conecte-se com um amigo ou familiar.",
            "Sunday": "Descanse e recarregue suas energias."
        }

        # Cria os widgets da interface
        self.criar_widgets()

    def criar_widgets(self):
        """Cria os elementos da interface gráfica."""
        self.intro_label = tk.Label(self.root, text="Bem-vindo ao sistema DASS-21", font=("Arial", 16))
        self.intro_label.pack(pady=20)

        self.botao_login = tk.Button(self.root, text="Login", command=self.exibir_login)
        self.botao_login.pack(pady=10)

        self.botao_cadastrar_usuario = tk.Button(self.root, text="Cadastrar Usuário", command=self.cadastrar_usuario)
        self.botao_cadastrar_usuario.pack(pady=10)

        self.botao_cadastrar_psicologo = tk.Button(self.root, text="Cadastrar Psicólogo",
                                                   command=self.cadastrar_psicologo)
        self.botao_cadastrar_psicologo.pack(pady=10)

    def exibir_login(self):
        """Exibe a tela de login."""
        self.limpar_tela()

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=5)

        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack(pady=5)

        self.botao_entrar = tk.Button(self.root, text="Entrar", command=self.verificar_login)
        self.botao_entrar.pack(pady=20)

        #Botão de voltar
        self.botao_voltar = tk.Button(self.root, text="Voltar",command=lambda: [self.limpar_tela(), self.criar_widgets()])
        self.botao_voltar.pack(pady=10)

    def verificar_login(self):
        """Verifica as credenciais do usuário."""
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if self.autenticar_usuario(email, senha):
            self.mostrar_desafios_diarios()
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")

    def autenticar_usuario(self, email, senha):
        """Autentica o usuário com base nos dados cadastrados."""
        if not os.path.exists("usuarios.txt"):
            return False

        try:
            with open("usuarios.txt", "r") as file:
                for line in file:
                    partes = line.strip().split(",")
                    usuario_email, usuario_senha = partes[2], partes[4]
                    if email == usuario_email and senha == usuario_senha:
                        return True
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao verificar o usuário: {e}")

        return False

    def mostrar_desafios_diarios(self):
        """Exibe os desafios diários ao usuário."""

        dias_da_semana = { "Monday": "segunda-feira",
            "Tuesday": "terça-feira",
            "Wednesday": "quarta-feira",
            "Thursday": "quinta-feira",
            "Friday": "sexta-feira",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }

        self.limpar_tela()

        dia_atual = tk.Label(self.root, text=f"Hoje é {dias_da_semana[self.obter_dia_semana()]}")
        dia_atual.pack(pady=10)

        desafio_label = tk.Label(self.root, text=f"Desafio do dia: {self.desafios[self.obter_dia_semana()]}")
        desafio_label.pack(pady=20)

        self.botao_iniciar_teste = tk.Button(self.root, text="Iniciar Teste DASS-21", command=self.iniciar_teste)
        self.botao_iniciar_teste.pack(pady=20)

        self.botao_agendar_horario = tk.Button(self.root, text="Agendar Horário", command=self.exibir_agendamento)
        self.botao_agendar_horario.pack(pady=10)

        self.botao_voltar = tk.Button(self.root, text="Deslogar", command=lambda: [self.limpar_tela(), self.criar_widgets()])
        self.botao_voltar.pack(pady=10)

    def obter_dia_semana(self):
        """Retorna o nome do dia da semana atual."""
        import datetime
        return datetime.datetime.now().strftime("%A")

    def exibir_agendamento(self):
        """Exibe a tela de agendamento de horário."""
        self.limpar_tela()

        self.label_escolha_psicologo = tk.Label(self.root, text="Escolha um Psicólogo:")
        self.label_escolha_psicologo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        # Carregar psicólogos do arquivo
        psicologos = self.carregar_psicologos()

        if not psicologos:
            messagebox.showerror("Erro",
                                 "Nenhum psicólogo cadastrado. Por favor, adicione um psicólogo antes de agendar.")
            self.mostrar_desafios_diarios()
            return

        self.psicologo_selecionado = tk.StringVar(self.root)
        self.psicologo_selecionado.set(psicologos[0])  # Define o primeiro psicólogo como padrão

        for i, psicologo in enumerate(psicologos):
            rb = tk.Radiobutton(self.root, text=psicologo, variable=self.psicologo_selecionado, value=psicologo,
                                command=self.atualizar_horarios_disponiveis)
            rb.grid(row=i + 1, column=0, padx=10, pady=2, sticky=tk.W)

        self.label_escolha_dia = tk.Label(self.root, text="Escolha um Dia da Semana:")
        self.label_escolha_dia.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
        self.dia_selecionado = tk.StringVar(self.root)
        self.dia_selecionado.set(dias[0])  # Define o primeiro dia como padrão

        for i, dia in enumerate(dias):
            rb = tk.Radiobutton(self.root, text=dia, variable=self.dia_selecionado, value=dia,
                                command=self.atualizar_horarios_disponiveis)
            rb.grid(row=i + 1, column=1, padx=10, pady=2, sticky=tk.W)

        self.label_escolha_horario = tk.Label(self.root, text="Escolha um Horário:")
        self.label_escolha_horario.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        # Atualiza a lista de horários disponíveis com base na seleção
        self.atualizar_horarios_disponiveis()

        self.botao_confirmar_agendamento = tk.Button(self.root, text="Confirmar Agendamento",
                                                     command=self.salvar_agendamento)
        self.botao_confirmar_agendamento.grid(row=len(dias) + 1, column=0, columnspan=3, pady=20)

        self.botao_voltar = tk.Button(self.root, text="Voltar",
                                      command=lambda: [self.limpar_tela(), self.mostrar_desafios_diarios()])
        self.botao_voltar.grid(row=len(dias) + 2, column=0, columnspan=3, pady=10)

    def atualizar_horarios_disponiveis(self):
        """Atualiza a lista de horários disponíveis com base na seleção do psicólogo e dia."""
        psicologo = self.psicologo_selecionado.get()
        dia = self.dia_selecionado.get()

        horarios_disponiveis = ["Manhã - 08:00", "Tarde - 14:00"]

        if psicologo and dia:
            try:
                with open("agendamentos.txt", "r") as file:
                    agendamentos = file.readlines()
                    for agendamento in agendamentos:
                        partes = agendamento.strip().split(",")
                        if len(partes) == 3:
                            ag_psicologo, ag_horario, ag_dia = partes
                            if psicologo == ag_psicologo and dia == ag_dia:
                                if ag_horario in horarios_disponiveis:
                                    horarios_disponiveis.remove(ag_horario)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar os agendamentos: {e}")

        # Remove widgets antigos de horários e cria novos
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Radiobutton) and widget.cget("text").startswith("Manhã") or widget.cget(
                    "text").startswith("Tarde"):
                widget.grid_forget()

        self.horario_selecionado = tk.StringVar(self.root)
        if horarios_disponiveis:
            self.horario_selecionado.set(horarios_disponiveis[0])  # Define o primeiro horário como padrão

            for i, horario in enumerate(horarios_disponiveis):
                rb = tk.Radiobutton(self.root, text=horario, variable=self.horario_selecionado, value=horario)
                rb.grid(row=i + 1, column=2, padx=10, pady=2, sticky=tk.W)
        else:
            self.horario_selecionado.set("")  # Nenhum horário disponível

    def carregar_psicologos(self):
        """Carrega os psicólogos cadastrados do arquivo."""
        psicologos = []
        if os.path.exists("psicologos.txt"):
            with open("psicologos.txt", "r") as file:
                for line in file:
                    partes = line.strip().split(",")
                    if len(partes) == 2:  # Espera-se que haja Nome e CRP
                        psicologos.append(partes[0])  # Adiciona o nome do psicólogo à lista
        return psicologos

    def salvar_agendamento(self):
        """Salva o agendamento no arquivo e atualiza a disponibilidade de horários."""
        psicologo = self.psicologo_selecionado.get()
        horario = self.horario_selecionado.get()
        dia = self.dia_selecionado.get()

        try:
            # Verifica se o agendamento já existe
            with open("agendamentos.txt", "r") as file:
                for line in file:
                    partes = line.strip().split(",")
                    if len(partes) == 3:  # Espera-se que haja Psicólogo, Horário e Dia
                        ag_psicologo, ag_horario, ag_dia = partes
                        if (psicologo == ag_psicologo and horario == ag_horario and dia == ag_dia):
                            messagebox.showerror("Erro", "Este horário já está agendado.")
                            return

            # Verifica se o dia é domingo e limpa o arquivo de agendamentos
            if self.obter_dia_semana() == "Sunday":
                open("agendamentos.txt", "w").close()  # Limpa o arquivo

            # Salva o novo agendamento
            with open("agendamentos.txt", "a") as file:
                file.write(f"{psicologo},{horario},{dia}\n")
            messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
            self.limpar_tela()
            self.mostrar_desafios_diarios()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o agendamento: {e}")

    def cadastrar_usuario(self):
        """Exibe a tela de cadastro de usuário."""
        self.limpar_tela()

        self.label_nome = tk.Label(self.root, text="Nome Completo:")
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack(pady=5)

        self.label_cpf = tk.Label(self.root, text="CPF:")
        self.label_cpf.pack(pady=5)
        self.entry_cpf = tk.Entry(self.root)
        self.entry_cpf.pack(pady=5)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=5)

        self.label_data_nascimento = tk.Label(self.root, text="Data de Nascimento:")
        self.label_data_nascimento.pack(pady=5)
        self.entry_data_nascimento = tk.Entry(self.root)
        self.entry_data_nascimento.pack(pady=5)

        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack(pady=5)

        self.botao_salvar = tk.Button(self.root, text="Cadastrar", command=self.salvar_usuario)
        self.botao_salvar.pack(pady=20)

        #Botão de voltar
        self.botao_voltar = tk.Button(self.root, text="Voltar", command=lambda: [self.limpar_tela(), self.criar_widgets()])
        self.botao_voltar.pack(pady=10)

    def salvar_usuario(self):
        """Salva os dados do usuário no arquivo de usuários."""
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        data_nascimento = self.entry_data_nascimento.get()
        senha = self.entry_senha.get()

        # Validação dos dados
        if len(nome) > 60:
            messagebox.showerror("Erro", "Nome completo excede o limite de 60 caracteres.")
            return
        if len(cpf) != 11 or not cpf.isdigit():
            messagebox.showerror("Erro", "CPF inválido: deve conter 11 dígitos numéricos.")
            return
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            messagebox.showerror("Erro", "Email inválido: formato incorreto.")
            return
        if len(senha) < 8:
            messagebox.showerror("Erro", "A senha deve conter no mínimo 8 digitos.")

        if not nome or not cpf or not email or not data_nascimento or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        # Verificação de duplicidade de CPF ou Email
        try:
            if os.path.exists("usuarios.txt"):
                with open("usuarios.txt", "r") as file:
                    for line in file:
                        partes = line.strip().split(",")
                        if len(partes) == 5:  # Espera-se que haja nome, cpf, email, data_nascimento e senha
                            usuario_cpf, usuario_email = partes[1], partes[2]
                            if cpf == usuario_cpf:
                                messagebox.showerror("Erro", "Este CPF já está cadastrado.")
                                return
                            if email == usuario_email:
                                messagebox.showerror("Erro", "Este email já está cadastrado.")
                                return

            # Salvando o usuário se não houver duplicidade
            with open("usuarios.txt", "a") as file:
                file.write(f"{nome},{cpf},{email},{data_nascimento},{senha}\n")
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.exibir_login()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o usuário: {e}")

    def cadastrar_psicologo(self):
        """Exibe a tela de cadastro de psicólogo."""
        self.limpar_tela()

        self.label_nome = tk.Label(self.root, text="Nome Completo:")
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack(pady=5)

        self.label_crp = tk.Label(self.root, text="CRP:")
        self.label_crp.pack(pady=5)
        self.entry_crp = tk.Entry(self.root)
        self.entry_crp.pack(pady=5)

        self.botao_salvar = tk.Button(self.root, text="Cadastrar", command=self.salvar_psicologo)
        self.botao_salvar.pack(pady=20)

        #Botão de voltar
        self.botao_voltar = tk.Button(self.root, text="Voltar", command=lambda: [self.limpar_tela(), self.criar_widgets()])
        self.botao_voltar.pack(pady=10)

    def salvar_psicologo(self):
        """Salva os dados do psicólogo no arquivo de psicólogos."""
        nome = self.entry_nome.get()
        crp = self.entry_crp.get()

        # Verifica o tamanho do nome do psicólogo
        if len(nome) > 60:
            messagebox.showerror("Erro", "Nome completo excede o limite de 60 caracteres.")
            return
        # Verifica o formato do CRP
        if not re.match(r"^06/\d{3}\.\d{3}$", crp):
            messagebox.showerror("Erro", "CRP inválido: o formato correto é 06/XXX.XXX.")
            return

        # Verifica se o CRP já está cadastrado
        try:
            with open("psicologos.txt", "r") as file:
                for line in file:
                    partes = line.strip().split(",")
                    if len(partes) == 2:  # Espera-se que haja nome e CRP
                        psicologo_crp = partes[1]
                        if crp == psicologo_crp:
                            messagebox.showerror("Erro", "Já existe um psicólogo cadastrado com este CRP.")
                            return
        except FileNotFoundError:
            pass

        try:
            with open("psicologos.txt", "a") as file:
                file.write(f"{nome},{crp}\n")
            messagebox.showinfo("Sucesso", "Psicólogo cadastrado com sucesso!")
            self.limpar_tela()
            self.criar_widgets()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o psicólogo: {e}")

    def iniciar_teste(self):
        """Inicia o teste DASS-21."""
        self.pergunta_atual = 0
        self.respostas = []
        self.mostrar_proxima_pergunta()

    def mostrar_proxima_pergunta(self):
        """Mostra a próxima pergunta do teste."""
        if self.pergunta_atual < len(self.perguntas):
            self.exibir_janela_pergunta(self.perguntas[self.pergunta_atual])
        else:
            self.calcular_resultado()

    def exibir_janela_pergunta(self, pergunta):
        """Exibe uma nova janela para cada pergunta."""
        pergunta_janela = tk.Toplevel(self.root)
        pergunta_janela.title(f"Pergunta {self.pergunta_atual + 1}")

        label_pergunta = tk.Label(pergunta_janela, text=pergunta)
        label_pergunta.pack(pady=20)

        # Variável para armazenar a resposta do usuário
        resposta = tk.StringVar()
        resposta.set("0")  # Resposta padrão

        # Opções de resposta
        opcoes = ["1 - Não se aplicou de maneira alguma",
                  "2 - Aplicou-se em algum grau, ou por pouco tempo",
                  "3 - Aplicou-se em um grau considerável, ou por uma boa parte do tempo",
                  "4 - Aplicou-se muito, ou na maioria do tempo"]

        for opcao in opcoes:
            rb = tk.Radiobutton(pergunta_janela, text=opcao, variable=resposta, value=opcoes.index(opcao))
            rb.pack(anchor=tk.W, pady=2)

        # Botão para próxima pergunta
        botao_proxima = tk.Button(pergunta_janela, text="Próxima",
                                  command=lambda: self.proxima_pergunta(pergunta_janela, resposta))
        botao_proxima.pack(pady=10)

    def proxima_pergunta(self, janela, resposta):
        """Processa a resposta e avança para a próxima pergunta."""
        self.respostas.append(int(resposta.get()))
        self.pergunta_atual += 1
        janela.destroy()
        self.mostrar_proxima_pergunta()

    def calcular_score(self, respostas, indices):
        """Calcula o score para um conjunto de respostas."""
        score = 0
        for i in indices:
            if respostas[i] == 1:
                score += 2
            elif respostas[i] == 2:
                score += 4
            elif respostas[i] == 3:
                score += 6
        return score

    def classificar(self, score, tipo):
        """Classifica o score de acordo com as escalas de DASS-21."""

        if tipo == "depressao":
            if 10 > score >= 0:
                return "Normal"
            elif 14 > score >= 10:
                return "Suave"
            elif 20 > score >= 14:
                return "Moderado"
            elif 28 > score >= 20:
                return "Severo"
            else:
                return "Extremamente Severo"

        elif tipo == "ansiedade":
            if 8 > score >= 0:
                return "Normal"
            elif 10 > score >= 8:
                return "Suave"
            elif 16 > score >= 10:
                return "Moderado"
            elif 20 > score >= 16:
                return "Severo"
            else:
                return "Extremamente Severo"

        elif tipo == "estresse":
            if 8 > score >= 0:
                return "Normal"
            elif 10 > score >= 8:
                return "Suave"
            elif 16 > score >= 10:
                return "Moderado"
            elif 20 > score >= 16:
                return "Severo"
            else:
                return "Extremamente Severo"
    def calcular_resultado(self):

        indices_ansiedade = [1, 3, 6, 8, 14, 18, 19]
        indices_depressao = [2, 4, 9, 12, 15, 16, 20]
        indices_estresse = [0, 5, 7, 10, 11, 13, 17]

        score_depressao = self.calcular_score(self.respostas, indices_depressao)
        score_ansiedade = self.calcular_score(self.respostas, indices_ansiedade)
        score_estresse = self.calcular_score(self.respostas, indices_estresse)

        """Calcula e exibe o resultado do teste."""

        resultado = {
            "depressao": self.classificar(score_depressao, "depressao"),
            "ansiedade": self.classificar(score_ansiedade, "ansiedade"),
            "estresse": self.classificar(score_estresse, "estresse")
        }

        maior_nivel = max(resultado.values(),
                          key=lambda nivel: ["Normal", "Suave", "Moderado", "Severo", "Extremamente Severo"].index(
                              nivel))

        messagebox.showinfo("Resultado", f"Depressão: {resultado['depressao']}\n"
                                         f"Ansiedade: {resultado['ansiedade']}\n"
                                         f"Estresse: {resultado['estresse']}\n\n"
                                         f"Recomendação: {self.recomendacoes[maior_nivel]}")

    def limpar_tela(self):
        """Remove todos os widgets da janela principal."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x450")  # Define um tamanho inicial para a janela
    app = DASS21App(root)
    root.mainloop()
