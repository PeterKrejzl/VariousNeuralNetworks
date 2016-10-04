##Can Artificial Intelligence replace politicians?

Deep Learning and the methods based on the neural networks are really popular these days. Almost looks like the company that does not use neural networks to support their business has no chance :)

There is a real boom of deep-learning methods, involving a lot of research in the area of algorithms as well as hardware supporting their huge computational needs. Not even talking about the availability of huge datasets used to train these networks.
Big companies like Google or Facebook have their own (big) teams working on deep learning, a lot of work is being done in academic sphere as well.

However, the idea of software simulating a human brain is not new, people were always fascinated how a brain works and it was considered as something like an ultimate goal for many decades.

We are not that far :)

In this post I’m not going to explain the technical details (maybe later :)), there are many tutorials around. I would just like to share some my excitement I experienced when playing with them.

Especially, I looked at so called recurrent neural networks (RNN) that belong to most complicated among all others. On the other hand, they can bring very interesting results.
Generally, to fully understand this area some knowledge of linear algebra is needed but usually it is nothing more complex than just some matrix and vector multiplications.

There is a very interesting implementation done by [Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) who trained the character level neural network. Character in this context means it works with characters and not for example whole words. After learning from some text (can be almost anything), the network generates one character at the time and the result is influenced not only by the input but also (here’s the recurrence) by the entire history of previous inputs. 

Sounds complicated? It’s not :) Basically, the network will based on the training text generate some other text. It has no information about the grammar, it knows nothing about the text itself, it just observes and learns from the examples we provided.

Let’s get back to my question from the title - is it possible to replace politicians? I took data set from European Parliament and trained the network on that. The dataset contains about 300MB of text, basically the transcriptions of speeches held in Parliament in 2011.
The network generated it’s own speech, character by character. 

Here’s an example:

```
Mr President, it is a special request in this House to the individual political party and non-regulated world, 
and we are prepared to see that it objections on the agenda and the region and the successful 
contents of the European Union to the country in the distribution of reserve to decision to the EU 
and the problem of the textile flexibility of the unemployment of the Union.
We should not be addressing the country from a country and we should now contribute 
to the control of the conclusion that it is a question to the protocol the services of 
the European Union and other sectors.
```

As you can see it looks like English text but almost completely meaningless. Well, the truth is that original transcriptions from the parliament are meaningless for me as well :) But we can clearly see that just based on characters, the network is following some sort of English grammar like capital letter at the beginning and generally the text really looks like an English.
Depending how conservative the model is, it can also from time to time generate some new words or unexpected phrases.

```I would like to say that the EU is currently being interconsulting the programme in the world.```

Also we can see the network (as well as all politicians!) really likes very long sentences:

```
However, I would like to finish the contributions on the British people of the French and 
the agenda of the European Union on the Council in the world who live in the funds 
in the entrepreneurs of the new Member States, such as children and consumer groups and 
political money, which does not mean that there are some exception of the control 
of the timeshare - it takes approach that the Directorate-General of the European Union 
can be prevented from the press.
Moreover, the EU is entirely difficult to make a comprehensive internal care for 
the new Member States, and despite its humanitarian aid, which is concerned to include 
a large number of countries.
The Commission will have a great deal of personal matters which means in our country, 
which will become a political framework of the European Council to take action against 
increasing the Union may not be accepted, with the interests of the European Union 
and the report and the Commission to speak on both amendments, the Commission can only 
be a part of peace and the money for example of the counterparts of the EU, which has 
been in additional guidelines in Guinea and the United States to the people of 
European integration.
The agreement will be able to provide a renewable energy definition of the funds.
There are a response for the situation in the complaints of the Community institutional 
representation of the International Affairs Council and the Commission the Commission 
on the report was not accommodated to the rapporteur, Mr President, ladies and gentlemen, 
in the context of the programmes and optimism, which is not only the decision of the President.
```




This should be really just a funny example of a network creating its own language model but such a thing can be coded in minutes and trained in a couple of hours.


It similarly (in a funny way) works with the source code. I took a couple of megabytes of the code of our stored procedures and got very similar and interesting results. Obviously, the SQL or any other programming language it a bit more strict but the generated procedures were very to close to be compiled :)



And because I had to somehow defend the evenings spending reading and playing with the deep learning techniques, especially for my wife I trained one more model based on the [Jane Austin] (https://www.facebook.com/JaneAustenAuthor/?fref=ts) novels. So, from the European Parliament back to the world of `“Sense and Sensibility”`, `“Pride and Prejudice”` and `“Persuasion”`.
-> ![alt text](https://github.com/PeterKrejzl/VariousNeuralNetworks/blob/master/img/Jane_Austen_coloured_version.jpg "Jane Austin") <-


Here are some examples (same as before- I have no clue what this is about :) )

```
Mrs. Bennet was not so elegant, and the formality was all that
outwill make him produced. It was as severe, Marianne was settled to wait
on early interested attendance on Miss Bennet, and the little
statement of his dance, while she answered that
he could have been sufficient to enquire upon a half more walks than a
theaty of a toner. Mrs. Phison's manners tooke the children of his friend. He
made no answer, and each of them darlied.

Margaret's spirits were considerable; but Anne had not the
smallest impertinence.

"And they are made no more of the lace did not stopped, and promise me to me.  If I were
inquiring Miss Bingley?"

Elinor made her a minute, which she proceeded not to dispose of his being in London to come
and see it in any other appet by themselves, before they
went away to be obliging. She could not even thank her upsigness.

Colonel Brandon's spirits exclaimed in a different consequence.

"I was within a time, if you do not think an unfortunate asking me
to pound. But, does Lady Russell and health and dislike."

"Mr. Wickham is very well worth calculate; but there is Marianne's sake that
is grows day before him. My understanding and esteam
it would have been sufficient."

"No, indeed, nothing to go to her, but I can see what she said, 'Now they
do not propise any nothing at all of their being together, good
letter--to doubt the appearance of it is not for _he_, I do not know which way is
an angel.
```


There are many interesting applications of this approach. Jiri Materna from seznam.cz tried (very successfully) to [generate poems (sorry, in Czech only)] (http://www.kosmas.cz/knihy/216522/poezie-umeleho-sveta/). 
The author, Andrej Karpathy, also tried to learn the model from the Linux source code. I’m pretty sure there are many interesting and funny use cases. 

I might generate some fake resumes and check if recruiters notice :) :) :)

