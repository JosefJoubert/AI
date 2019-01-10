function [weights, bias] = Training(Data) 
    weights(2,9,6) = 0;
    sigma(8) = 0;
    hidden(6) = 0;
    outputs(2) = 0;
    error(8) = 0;
    bias(8) = 0;
    
    for a=1:2
       for b=1:9
          for c=1:6
              weights(a,b,c) = (2*rand-1)/sqrt(6); 
          end
       end
    end
    for a=1:8
       bias(a) =  (2*rand-1)/sqrt(6);
    end
    
    training = 0.01;
    
    for a=1:350
        for b=1:6
            sigma(b) = 0;
            for c=1:9
               sigma(b) = Data(a,c)*weights(1,c,b) + sigma(b) + bias(b); 
            end
            hidden(b) = tanh(sigma(b));
        end
        for b=1:2
           sigma(6+b) = 0;
           for c=1:6
              sigma(6+b) = hidden(c)*weights(2,c,b) + bias(6+b); 
           end
           outputs(b) = tanh(sigma(6+b));
           error(6+b) = (Data(a,9+b) - outputs(b));
        end
        
        range(a) = a;
        plots(a) = error(8)/2 + error(7)/2;
        plot(range,plots)
        
        delta(7) = error(7)*(1-(tan(sigma(7)).^2));
        delta(8) = error(8)*(1-(tan(sigma(8)).^2));
        bias(7) = bias(7) + delta(7)*training;
        bias(8) = bias(8) + delta(8)*training;
        
        for b=1:2
            for c=1:6
               weights(2,c,b) = weights(2,c,b) + delta(6+b)*training*hidden(c); 
            end
        end
        for b=1:6
           error(b) = weights(2,b,1)*delta(7) + weights(2,b,2)*delta(8); 
           delta(b) = error(b)*(1-(tan(sigma(b)).^2));
        end

        for b=1:6
            bias(b) = bias(b) + training*delta(b);
            for c=1:9
                weights(1,c,b) = weights(1,c,b) + delta(b)*training*Data(c);
            end
        end       
    end
end